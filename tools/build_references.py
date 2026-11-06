"""Regenerate docs/references.html from the reference lists of every ready chapter.

Run from the repository root: python3 tools/build_references.py
The "Core reading" list at the top is kept as written; everything after it is rebuilt.
"""
import re, glob, html

page = open('docs/references.html').read()
head, rest = page.split('<div class="cover">', 1)
core = rest[:rest.index('<h2>History of agents</h2>')] if '<h2>History of agents</h2>' in rest else rest[:rest.index('<h2 id="by-chapter">')]

js = open('docs/assets/js/book.js').read()
titles = {m.group(1): m.group(2) for m in re.finditer(r"id: '(ch\d+)', n: \d+, part: '[IVX]+', title: '([^']+)'", js)}

out = ['<h2 id="by-chapter">References by chapter</h2>',
       '<p class="small muted">Each chapter\'s primary sources, in order of first citation. Links open the chapter.</p>']
seen = set()
for path in sorted(glob.glob('docs/chapters/ch*.html')):
    s = open(path).read()
    cid = re.search(r'data-chapter="(ch\d+)"', s).group(1)
    n = int(cid[2:])
    if 'id="references"' not in s:
        continue
    block = s[s.index('<ol class="refs">', s.index('id="references"')):]
    block = block[:block.index('</ol>')]
    items = re.findall(r'<li id="ref-[^"]+">(.*?)</li>', block, flags=re.S)
    out.append('<h3><a href="chapters/%s.html">Chapter %d — %s</a></h3>' % (cid, n, titles.get(cid, '')))
    out.append('<ol class="refs">')
    for it in items:
        key = re.sub(r'<[^>]+>', '', it)[:80].lower()
        mark = '' if key not in seen else ' <span class="muted small">(also cited earlier)</span>'
        seen.add(key)
        out.append('<li>%s%s</li>' % (it.strip(), mark))
    out.append('</ol>')

page = head + '<div class="cover">' + core + '\n'.join(out) + '\n</div>\n</body>\n</html>\n'
open('docs/references.html', 'w').write(page)
print('wrote docs/references.html with', len(seen), 'distinct references')
