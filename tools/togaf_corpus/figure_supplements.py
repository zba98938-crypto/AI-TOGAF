"""Transcriptions visually checked against the original PDF image regions.

Each change is bound to a source SHA256 in figure-supplements.json. Color checking
is independent validation of the manually transcribed G198 numeric matrix cells.
"""
from pathlib import Path
import json
from collections import Counter
from PIL import Image

DATA = json.loads(Path(__file__).with_name('figure-supplements.json').read_text())


def enrich_image(item, image_path):
    code = item['document_id']; page = item['pdf_page']; fid = item['id']
    if item['provenance']['pdf_sha256'] != DATA['source_sha256'].get(code):
        return
    review = {'status': 'visually-transcribed-from-original-source', 'scope': 'image-purpose-and-visible-labels',
              'evidence': 'original PDF crop', 'source_pdf_sha256': item['provenance']['pdf_sha256']}
    specific = DATA['images'].get(fid)
    if specific:
        item.update(specific)
        if code == 'G198' and specific.get('tables') and page != 15:
            table = specific['tables'][0]
            im = Image.open(image_path).convert('RGB')
            palette = {(255,243,131): 1, (176,203,31): 2, (118,144,201): 3, (234,85,111): 4}
            w, h = im.size; ys = [y for y in range(h) if im.getpixel((int(w*.195),y)) in palette]
            a, b = min(ys), max(ys)+1
            mismatches = []
            for r, row in enumerate(table['rows']):
                cy = a + (b-a)*(r+.5)/len(table['rows'])
                for c, expected in enumerate(row[1:]):
                    cx = w*(.181+(c+.5)*.819/10)
                    pixels = im.crop((int(cx-12),int(cy-5),int(cx+12),int(cy+5)))
                    counts = Counter(palette[x] for x in pixels.getdata() if x in palette)
                    actual = counts.most_common(1)[0][0] if counts else None
                    if actual != expected:
                        mismatches.append({'row': r+1, 'column': c+1, 'expected': expected, 'observed_color_level': actual})
            review['numeric_cell_check'] = {'method': 'independent cell-background color comparison against level legend',
                                             'checked_cells': len(table['rows'])*10, 'mismatches': mismatches}
            if mismatches:
                raise ValueError(f'{fid}: numeric transcription differs from source colors: {mismatches}')
        item['current_visual_review'] = review
        return
    if page == 1:
        item['description_zh'] = '封面品牌图：The Open Group 标识和 The TOGAF Standard – 10th Edition 字样。用于识别出版系列，不表达架构节点或关系。'
        item['visible_labels'] = ['The Open Group', 'The TOGAF Standard – 10th Edition']
        item['image_kind'] = 'cover-branding'
    elif code == 'G188':
        item['description_zh'] = '蓝色圆形内白色小写 i，表示旁边文字为信息提示。该图标不构成业务模型或流程节点。'
        item['image_kind'] = 'information-callout-icon'
    elif code == 'G242':
        item['description_zh'] = '图钉固定便签纸的灰色提示图标；用于标记正文说明，不表达架构关系。'
        item['image_kind'] = 'note-callout-icon'
    elif code == 'G212' and 28 <= page <= 38:
        item['description_zh'] = '三个人物上方有灯泡和闪电的黑色提示图标，用于伴随数字技术采用因素的说明。图中没有可读文字或连线关系。'
        item['image_kind'] = 'factor-callout-icon'
    elif code == 'G212' and 49 <= page <= 56:
        item['description_zh'] = '问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。'
        item['image_kind'] = 'likert-response-scale'
        item['ordered_options'] = ['Strongly Agree', 'Agree', 'Somewhat Agree', 'Neutral', 'Somewhat Disagree', 'Disagree', 'Strongly Disagree']
        item['selected_option'] = None
    else:
        return
    item['current_visual_review'] = review
