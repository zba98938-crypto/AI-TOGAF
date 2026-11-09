"""Check local Markdown destinations without a dependency on development tests."""
from pathlib import Path
import re
from urllib.parse import unquote
from html.parser import HTMLParser


# Match the destination delimiter, independently of brackets inside the label.
# This also handles image labels such as ![caption [C220]](figure.svg).
MARKDOWN_LINK_PATTERN = re.compile(r'(\]\()([^\n)]+)(\))')


def markdown_destinations(text):
    """Local resource syntax used by retained Markdown, with stable byte offsets."""
    destinations=[(match.start(2),match[2]) for match in MARKDOWN_LINK_PATTERN.finditer(text)]
    definitions={}
    for match in re.finditer(r'^ {0,3}\[([^\]\n]+)\]:\s*(<[^>\n]+>|\S+)',text,re.M):
        definitions[match[1].strip().casefold()]=(match.start(2),match[2])
    for match in re.finditer(r'!?\[([^\]\n]+)\](?:\[([^\]\n]*)\])?',text):
        if text[match.end():].startswith(('(',':')):continue
        key=(match[2] or match[1]).strip().casefold()
        if key in definitions:destinations.append(definitions[key])
    line_offsets=[0]+[match.end() for match in re.finditer('\n',text)]
    class Resources(HTMLParser):
        def handle_starttag(self,tag,attrs):
            attributes=dict(attrs)
            names={'img':('src','srcset'),'source':('src','srcset'),
                   'a':('href',),'video':('src','poster'),'audio':('src',),
                   'object':('data',),'embed':('src',),'link':('href',),'iframe':('src',)}.get(tag,())
            if not names:return
            line,column=self.getpos();offset=line_offsets[line-1]+column
            for name in names:
                value=attributes.get(name)
                if value is None:continue
                if name=='srcset':
                    destinations.extend((offset,item.strip().split()[0]) for item in value.split(',') if item.strip())
                else:destinations.append((offset,value))
    parser=Resources(convert_charrefs=True);parser.feed(text)
    return sorted(set(destinations))


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
        for _,target in markdown_destinations(path.read_text(encoding='utf-8')):
            target = target.strip().split(' "')[0].strip('<>')
            if re.match(r'^[a-z][a-z0-9+.-]*:', target, re.I) or target.startswith('#'):
                continue
            local = unquote(target.split('#', 1)[0])
            if local and not (path.parent / local).exists():
                broken.append({'file': str(path.relative_to(directory)), 'target': target})
    return broken
