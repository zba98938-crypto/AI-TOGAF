"""Read the complete local Markdown dependency graph without fetching resources."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import re
from collections import deque

from package_links import markdown_destinations, markdown_files


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dependency_root(corpus):
    corpus = Path(corpus).resolve()
    return corpus.parent if corpus.name == 'corpus' and corpus.parent.name == '_shared' else corpus


def has_symlink(path,boundary):
    """Packaging excludes aliases; reject them before resolving even internal ones."""
    path=Path(path)
    return path.is_symlink() or any(parent.is_symlink() for parent in path.parents
                                   if parent!=boundary and boundary in parent.parents)


def local_dependencies(corpus):
    """Return every occurrence, including missing/unsafe destinations as issues."""
    corpus = Path(corpus).resolve()
    boundary = dependency_root(corpus)
    edges, issues = [], []
    pending=deque(markdown_files(corpus));visited=set()
    while pending:
        document=pending.popleft()
        if document in visited:continue
        visited.add(document)
        if boundary not in document.resolve().parents or has_symlink(document,boundary):
            issues.append({'code': 'markdown-document-outside-package', 'document': str(document)})
            continue
        text = document.read_text(encoding='utf-8')
        document_internal=corpus in document.parents
        document_base=corpus if document_internal else boundary
        for offset,raw_target in markdown_destinations(text):
            target = raw_target.strip()
            target = (target[1:target.find('>')] if target.startswith('<') and '>' in target
                      else re.split(r'\s+[\"\']', target, maxsplit=1)[0])
            locator = {'document': document.relative_to(document_base).as_posix(),
                       'document_scope':'corpus' if document_internal else 'shared',
                       'offset':offset, 'target': target}
            try:
                decoded = unquote(target)
                if '\x00' in decoded or '\\' in decoded:
                    raise ValueError('invalid path')
                parsed = urlsplit(decoded)
                if parsed.scheme.lower() in {'http', 'https', 'mailto'}:
                    continue  # Historical external citations remain citations; never fetched.
                if parsed.scheme or parsed.netloc or parsed.query or Path(parsed.path).is_absolute():
                    raise ValueError('unsafe path or protocol')
                if not parsed.path:
                    continue
                lexical=document.parent/parsed.path
                if has_symlink(lexical,boundary):
                    issues.append({'code':'markdown-dependency-symlink',**locator});continue
                candidate = lexical.resolve()
                if boundary not in candidate.parents:
                    raise ValueError('path or symlink escapes package')
                internal = corpus in candidate.parents
                relative = candidate.relative_to(corpus if internal else boundary).as_posix()
                row = {**locator, 'scope': 'corpus' if internal else 'shared', 'package_path': relative}
                edges.append(row)
                if not candidate.is_file():
                    issues.append({'code': 'markdown-dependency-missing', **locator, 'package_path': relative})
                elif candidate.suffix.lower()=='.md' and candidate not in visited:
                    pending.append(candidate)
            except ValueError as exc:
                issues.append({'code': 'markdown-dependency-outside-package', **locator, 'detail': str(exc)})
    return edges, issues


def dependency_evidence(corpus):
    corpus = Path(corpus).resolve()
    boundary = dependency_root(corpus)
    edges, issues = local_dependencies(corpus)
    hashes = {}
    for row in edges:
        path = (corpus if row['scope'] == 'corpus' else boundary) / row['package_path']
        if row['scope']=='corpus' and row['package_path']=='source-map.json':
            row['kind']='source-map-self-reference'
            continue  # The complete manifest is hashed by the closure receipt, never by itself.
        if path.is_file():
            hashes.setdefault(path, digest(path))
            row['sha256'] = hashes[path]
    return edges, issues
