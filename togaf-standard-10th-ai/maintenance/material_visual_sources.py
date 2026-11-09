"""Locally render pinned W242C pages and identify every PDF image occurrence.

These are source-access evidence. Provisional background typing and successful
rendering do not grant semantic review, professional acceptance or signatures.
"""
from collections import Counter
import hashlib
import io
import json
import math
from pathlib import Path
import shutil
import subprocess
import tempfile

REPO = Path(__file__).resolve().parents[2]
PDF_PATH = 'togaf-standard-10th-ai/skills/_shared/corpus/sources/pdf/w242c.pdf'
PDF_SHA = 'c45186cb30ce0f2930cd5b97714d7b3e91b796dfeb86b3608eb1414bee7a4431'
EXTRACT_PATH = 'togaf-standard-10th-ai/maintenance/work/supplementary/W242C-source.json'
EXTRACT_SHA = '3d4f09da647b23dcbe959ecfc129cc7768f7ec969a686de2e4c6cc652585c43e'
DPI = 144


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b''): h.update(block)
    return h.hexdigest()


def local(name, root):
    if (not isinstance(name, str) or not name or Path(name).is_absolute()
            or any(part in ('', '.', '..') for part in name.split('/'))
            or any(c in name for c in ('\\', ':', '%', '\x00'))):
        raise ValueError('noncanonical derived image path')
    root = Path(root).resolve(); path = root
    for part in name.split('/'):
        path /= part
        if path.is_symlink(): raise ValueError('derived image symlink forbidden')
    if not path.resolve().is_relative_to(root): raise ValueError('derived image path escapes repository')
    return path


def reference(path, root):
    name = Path(path).absolute().relative_to(Path(root).resolve()).as_posix()
    return {'path': name, 'sha256': sha(local(name, root))}


def verify_ref(ref, root):
    if not isinstance(ref, dict) or set(ref) != {'path', 'sha256'}: raise ValueError('derived image reference malformed')
    path = local(ref['path'], root)
    if not path.is_file() or sha(path) != ref['sha256']: raise ValueError('derived source/image fingerprint differs')
    return path


def read(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result: raise ValueError('duplicate derived image JSON key')
            result[key] = value
        return result
    return json.loads(Path(path).read_text(encoding='utf-8'), object_pairs_hook=unique,
        parse_constant=lambda _: (_ for _ in ()).throw(ValueError('nonfinite derived geometry')))


def crop_geometry(bbox, page, pixels):
    if len(bbox) != 4 or any(type(v) not in (int, float) or not math.isfinite(v) for v in bbox):
        raise ValueError('invalid PDF occurrence geometry')
    x0, y0, x1, y1 = bbox; px0, py0, px1, py1 = page
    if x1 < x0 or y1 < y0 or px1 <= px0 or py1 <= py0: raise ValueError('inverted PDF geometry')
    clip = [max(x0, px0), max(y0, py0), min(x1, px1), min(y1, py1)]
    if clip[0] >= clip[2] or clip[1] >= clip[3]: return None, None
    sx, sy = pixels[0] / (px1 - px0), pixels[1] / (py1 - py0)
    box = [max(0, math.floor((clip[0] - px0) * sx)), max(0, math.floor((clip[1] - py0) * sy)),
           min(pixels[0], math.ceil((clip[2] - px0) * sx)), min(pixels[1], math.ceil((clip[3] - py0) * sy))]
    return clip, box


def occurrence_records(document):
    rows = []
    for page in document:
        rows.append([{key: value.hex() if isinstance(value, bytes) else list(value) if isinstance(value, tuple) else value
                      for key, value in item.items()} for item in page.get_image_info(hashes=True, xrefs=True)])
    return rows


def occurrence_type(page, record, counts):
    if counts[record['xref']] >= 20: return 'repeated-page-background'
    return 'cover-page-image' if page == 1 else 'unclassified-page-image'


def renderer():
    binary = shutil.which('pdftoppm')
    if not binary: raise ValueError('existing local pdftoppm is unavailable')
    binary = Path(binary).resolve()
    version = subprocess.run([str(binary), '-v'], capture_output=True, text=True, timeout=10, check=True)
    return {'path': str(binary), 'sha256': sha(binary), 'version': (version.stdout + version.stderr).strip()}


def render_pages(pdf, out, tool):
    out.mkdir(parents=True, exist_ok=False)
    argv = [tool['path'], '-f', '1', '-l', '40', '-r', str(DPI), '-png', str(pdf), str(out / 'page')]
    run = subprocess.run(argv, capture_output=True, text=True, timeout=180, check=True,
                         env={'PATH': '/opt/homebrew/bin:/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C'})
    files = sorted(out.glob('page-*.png'))
    if len(files) != 40: raise ValueError('W242C renderer did not produce all 40 pages')
    return files, {'argv': argv, 'exit_code': run.returncode, 'stdout': run.stdout, 'stderr': run.stderr}


def build(out, root=REPO):
    import fitz
    from PIL import Image
    root = Path(root).resolve(); out = Path(out)
    if not out.is_absolute(): out = root / out
    out = local(out.absolute().relative_to(root).as_posix(), root)
    if not out.is_relative_to(root / 'output'): raise ValueError('derived images must be in repository output')
    pdf = verify_ref({'path': PDF_PATH, 'sha256': PDF_SHA}, root)
    extraction = verify_ref({'path': EXTRACT_PATH, 'sha256': EXTRACT_SHA}, root); extracted = read(extraction)
    out.mkdir(parents=True, exist_ok=False); tool = renderer()
    images, command = render_pages(pdf, out / 'pages', tool)
    document = fitz.open(pdf); rows = occurrence_records(document)
    if len(document) != 40 or document.is_encrypted: raise ValueError('pinned W242C page scope differs')
    counts = Counter(item['xref'] for page in rows for item in {r['xref']: r for r in page}.values())
    pages = []; crops = out / 'occurrences'; crops.mkdir(); raw_cache = {}
    for index, (image_path, occurrences, original) in enumerate(zip(images, rows, extracted['pages'])):
        number = index + 1
        if original['pdf_page'] != number or original['image_count'] != len(occurrences):
            raise ValueError('W242C original image occurrence count differs')
        image = Image.open(image_path).convert('RGB'); geometry = list(document[index].rect)
        page = {'pdf_page': number, 'source_locator': {'json_pointer': '/pages/' + str(index), 'pdf_page': number},
                'page_bbox_pdf_points': geometry, 'pixels': list(image.size), 'primary_image': reference(image_path, root),
                'original_image_count': original['image_count'], 'occurrences': []}
        for item in occurrences:
            xref = item['xref']
            if not xref: raise ValueError('an inline PDF image requires an explicit extraction adapter')
            if xref not in raw_cache: raw_cache[xref] = hashlib.sha256(document.extract_image(xref)['image']).hexdigest()
            clip, box = crop_geometry(item['bbox'], geometry, image.size)
            crop_ref = None
            if box:
                crop = image.crop(box); encoded = io.BytesIO(); crop.save(encoded, format='PNG')
                path = crops / f'page-{number:02}-occurrence-{item["number"]:02}.png'; path.write_bytes(encoded.getvalue())
                crop_ref = reference(path, root)
            page['occurrences'].append({'id':f'W242C:p{number:04}:image-{item["number"]:03}', 'pdf_image': item,
                'raw_image_sha256': raw_cache[xref], 'provisional_type': occurrence_type(number, item, counts),
                'classification_status':'pending-independent-adjudication', 'clip_bbox_pdf_points':clip,
                'crop_box_pixels':box, 'crop_image':crop_ref, 'representation':'rendered-page-occurrence-crop'})
        pages.append(page)
    manifest = {'schema_version':'material-derived-page-images/1', 'document_id':'W242C',
        'source':reference(pdf, root), 'source_document':reference(extraction, root), 'renderer':tool,
        'dpi':DPI, 'render_command':command, 'pages':pages, 'page_count':40,
        'occurrence_count':sum(len(p['occurrences']) for p in pages), 'model_requests':0,
        'semantic_review_status':'pending', 'human_professional_acceptance':'pending_signature',
        'real_organization_approval':'pending_signature', 'fitz_version':list(fitz.version),
        'note':'Full-page rasters include text and vector drawings. PDF image occurrences often represent backgrounds; they are not all body figures.'}
    path = out / 'manifest.json'; path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    return reference(path, root)


def verify(reference_value, root=REPO, *, rerender=True):
    import fitz
    from PIL import Image
    root = Path(root).resolve(); path = verify_ref(reference_value, root); manifest = read(path)
    if (manifest.get('schema_version') != 'material-derived-page-images/1' or manifest.get('document_id') != 'W242C'
            or manifest.get('source') != {'path':PDF_PATH, 'sha256':PDF_SHA}
            or manifest.get('source_document') != {'path':EXTRACT_PATH, 'sha256':EXTRACT_SHA}
            or manifest.get('dpi') != DPI or manifest.get('page_count') != 40
            or manifest.get('semantic_review_status') != 'pending' or manifest.get('model_requests') != 0
            or manifest.get('human_professional_acceptance') != 'pending_signature'
            or manifest.get('real_organization_approval') != 'pending_signature'):
        raise ValueError('derived page manifest source/scope/status differs')
    pdf = verify_ref(manifest['source'], root); extracted = read(verify_ref(manifest['source_document'], root))
    document = fitz.open(pdf); rows = occurrence_records(document)
    counts = Counter(item['xref'] for page in rows for item in {r['xref']:r for r in page}.values())
    if len(manifest['pages']) != 40: raise ValueError('derived page closure differs')
    crops = 0; raw_cache = {}
    for index, (page, actual) in enumerate(zip(manifest['pages'], rows)):
        number = index + 1; original = extracted['pages'][index]
        if (page['pdf_page'] != number or page['source_locator'] != {'json_pointer':'/pages/' + str(index), 'pdf_page':number}
                or page['page_bbox_pdf_points'] != list(document[index].rect)
                or page['original_image_count'] != original['image_count'] or len(actual) != original['image_count']
                or len(page['occurrences']) != len(actual)):
            raise ValueError('derived page locator/original occurrence closure differs')
        image = Image.open(verify_ref(page['primary_image'], root)).convert('RGB')
        expected_size = [math.ceil(v * DPI / 72) for v in (document[index].rect.width, document[index].rect.height)]
        if page['pixels'] != list(image.size) or page['pixels'] != expected_size:
            raise ValueError('derived raster geometry differs')
        for item, record in zip(actual, page['occurrences']):
            xref = item['xref']
            if xref not in raw_cache: raw_cache[xref] = hashlib.sha256(document.extract_image(xref)['image']).hexdigest()
            clip, box = crop_geometry(item['bbox'], page['page_bbox_pdf_points'], image.size)
            if (record['pdf_image'] != item or record['raw_image_sha256'] != raw_cache[xref]
                    or record['clip_bbox_pdf_points'] != clip or record['crop_box_pixels'] != box
                    or record['id'] != f'W242C:p{number:04}:image-{item["number"]:03}'
                    or record['provisional_type'] != occurrence_type(number, item, counts)
                    or record['classification_status'] != 'pending-independent-adjudication'
                    or record['representation'] != 'rendered-page-occurrence-crop'):
                raise ValueError('derived crop/source occurrence binding differs')
            if box:
                crop = Image.open(verify_ref(record['crop_image'], root)).convert('RGB')
                expected = image.crop(box)
                if crop.size != expected.size or crop.tobytes() != expected.tobytes(): raise ValueError('derived crop pixels differ')
                crops += 1
            elif record['crop_image'] is not None: raise ValueError('off-page image has an invented visible crop')
    if manifest['occurrence_count'] != sum(len(r) for r in rows): raise ValueError('derived occurrence count differs')
    tool = renderer()
    if tool != manifest['renderer']: raise ValueError('existing local renderer identity changed')
    command = manifest['render_command']; argv = command['argv']
    if (len(argv) != 10 or argv[:8] != [tool['path'], '-f', '1', '-l', '40', '-r', str(DPI), '-png']
            or not argv[8].endswith('/' + PDF_PATH) or command['exit_code'] != 0
            or not isinstance(command['stdout'], str) or not isinstance(command['stderr'], str)):
        raise ValueError('derived image command is not the fixed local renderer invocation')
    recorded_root = argv[8][:-len(PDF_PATH)]
    retained_prefix = str(Path(manifest['pages'][0]['primary_image']['path']).parent / 'page')
    if argv[9] != recorded_root + retained_prefix:
        raise ValueError('derived renderer output path does not bind the retained page directory')
    if rerender:
        with tempfile.TemporaryDirectory(prefix='material-visual-verify-', dir=path.parent) as temporary:
            images, _ = render_pages(pdf, Path(temporary) / 'pages', tool)
            for page, actual_path in zip(manifest['pages'], images):
                retained = Image.open(verify_ref(page['primary_image'], root)).convert('RGB')
                actual = Image.open(actual_path).convert('RGB')
                if retained.size != actual.size or retained.tobytes() != actual.tobytes():
                    raise ValueError('derived page pixels do not reproduce from the pinned original PDF')
    return {'passed':True, 'page_count':40, 'occurrence_count':manifest['occurrence_count'], 'visible_crops':crops,
            'provisional_types':dict(Counter(r['provisional_type'] for p in manifest['pages'] for r in p['occurrences'])),
            'original_pdf_rerendered':rerender, 'semantic_review_status':'pending', 'model_requests':0}
