"""Check local Markdown destinations without a dependency on development tests."""
from pathlib import Path
import re
from urllib.parse import unquote


# Match the destination delimiter, independently of brackets inside the label.
# This also handles image labels such as ![caption [C220]](figure.svg).
MARKDOWN_LINK_PATTERN = re.compile(r'(\]\()([^\n)]+)(\))')


def markdown_files(directory, *, excluded_top_level=()):
    directory = Path(directory).resolve()
    for path in sorted(directory.rglob('*.md')):
        relative = path.relative_to(directory)
        if relative.parts[0] in excluded_top_level:
            continue
        if path.is_symlink() or any(part in {'.venv', 'node_modules', '.git', '__pycache__'} for part in relative.parts):
            continue
        yield path


def broken_markdown_links(directory, *, excluded_top_level=()):
    directory = Path(directory).resolve()
    broken = []
    for path in markdown_files(directory, excluded_top_level=excluded_top_level):
        for match in MARKDOWN_LINK_PATTERN.finditer(path.read_text(encoding='utf-8')):
            target = match[2]
            target = target.strip().split(' "')[0].strip('<>')
            if re.match(r'^[a-z][a-z0-9+.-]*:', target, re.I) or target.startswith('#'):
                continue
            local = unquote(target.split('#', 1)[0])
            if local and not (path.parent / local).exists():
                broken.append({'file': str(path.relative_to(directory)), 'target': target})
    return broken
