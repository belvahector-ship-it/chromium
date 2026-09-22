import re, json, pathlib
R = pathlib.Path('/root/.claude/skills/image-prompt-studio/references')

def sections(md):
    """Split markdown into {heading: body} for level-2 headings."""
    out, cur, buf = {}, None, []
    for line in md.split('\n'):
        m = re.match(r'^## (.+)$', line)
        if m:
            if cur: out[cur] = '\n'.join(buf)
            cur, buf = m.group(1).strip(), []
        elif cur is not None:
            buf.append(line)
    if cur: out[cur] = '\n'.join(buf)
    return out

def rows(body):
    """Pull data rows out of every pipe table in a section body."""
    out = []
    for line in body.split('\n'):
        line = line.strip()
        if not line.startswith('|'): continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if all(set(c) <= set('-: ') for c in cells): continue   # separator
        if cells and cells[0] in ('#', 'Kode'): continue        # header
        if len(cells) >= 2 and cells[1] in ('Kode', 'Kalimat prompt'): continue
        out.append(cells)
    return out

def clean(s):
    return s.replace('`', '').strip()

data = {}

# ---- 50 camera codes -------------------------------------------------
cam = sections((R/'camera-codes.md').read_text())
data['camera'] = []
for h, body in cam.items():
    m = re.match(r'^(\d\d) — (.+?) \(', h)
    if not m: continue
    group = m.group(2)
    for c in rows(body):
        if len(c) < 3 or not c[0].isdigit(): continue
        data['camera'].append({'n': int(c[0]), 'group': group,
                               'code': clean(c[1]), 'prompt': clean(c[2])})

# ---- lighting --------------------------------------------------------
lit = sections((R/'lighting.md').read_text())
LIT_MAP = {
    'Pola cahaya potret': 'Pola potret', 'Arah cahaya': 'Arah',
    'Kualitas cahaya': 'Kualitas', 'Rasio & mood': 'Rasio & mood',
    'Setup studio': 'Setup studio', 'Cahaya alami': 'Alami',
    'Cahaya buatan & berwarna': 'Buatan & warna', 'Mood sinematik': 'Sinematik',
    'Memperbaiki cahaya yang meleset': 'Perbaikan',
}
data['lighting'] = []
for h, label in LIT_MAP.items():
    for c in rows(lit.get(h, '')):
        if len(c) < 2: continue
        data['lighting'].append({'group': label, 'code': clean(c[0]),
                                 'prompt': clean(c[1]),
                                 'note': clean(c[2]) if len(c) > 2 else ''})

# ---- visual effects --------------------------------------------------
fx = sections((R/'visual-effects.md').read_text())
FX_MAP = {
    'Optik & lensa': 'Optik & lensa', 'Bokeh & kedalaman': 'Bokeh & kedalaman',
    'Gerakan': 'Gerakan', 'Tekstur film': 'Tekstur film',
    'Film stock': 'Film stock', 'Color grading': 'Color grading',
    'Atmosfer': 'Atmosfer', 'Teknik komposit': 'Komposit',
    'Gaya artistik': 'Gaya artistik',
}
data['effects'] = []
for h, label in FX_MAP.items():
    for c in rows(fx.get(h, '')):
        if len(c) < 2: continue
        data['effects'].append({'group': label, 'code': clean(c[0]),
                                'prompt': clean(c[1]),
                                'note': clean(c[2]) if len(c) > 2 else ''})

# ---- transform presets (### heading + blockquote) --------------------
tf = (R/'photo-transform.md').read_text()
data['presets'] = []
cur_group = ''
for block in re.split(r'\n(?=### )', tf):
    gm = re.findall(r'^## (.+)$', block, re.M)
    m = re.match(r'### (\d+)\. (.+)', block)
    if not m: continue
    quote = ' '.join(l.lstrip('> ').strip()
                     for l in block.split('\n') if l.startswith('>'))
    desc = ''
    for line in block.split('\n')[1:]:
        if line.startswith('>') or line.startswith('#'): break
        if line.strip(): desc += line.strip() + ' '
    data['presets'].append({'n': int(m.group(1)), 'name': m.group(2).strip(),
                            'desc': desc.strip(), 'prompt': quote.strip()})

# group presets by the ## section they fall under
order = re.findall(r'^(##|###) (.+)$', tf, re.M)
cur = ''
gmap = {}
for lvl, txt in order:
    if lvl == '##': cur = txt.strip()
    else:
        mm = re.match(r'(\d+)\.', txt)
        if mm: gmap[int(mm.group(1))] = cur
for p in data['presets']:
    p['group'] = gmap.get(p['n'], '').replace('Turunan: ', '').strip()
    if p['group'].startswith('Enam prompt'): p['group'] = 'Prompt inti'

# ---- angle change prompts --------------------------------------------
ac = (R/'angle-change.md').read_text()
data['angle'] = []
for m in re.finditer(r'## (Prompt [A-Z] — .+?)\n(.*?)(?=\n## |\Z)', ac, re.S):
    title = m.group(1).strip()
    body = m.group(2)
    desc = ''
    for line in body.split('\n'):
        if line.startswith('>'): break
        if line.strip(): desc += line.strip() + ' '
    quote = ' '.join(l.lstrip('> ').strip() for l in body.split('\n') if l.startswith('>'))
    if not quote: continue
    data['angle'].append({'code': title.replace('Prompt ', '').strip(),
                          'group': 'Ubah sudut', 'desc': re.sub(r'\*\*|\*', '', desc).strip(),
                          'prompt': quote.strip(), 'note': ''})

# ---- identity lock levels -------------------------------------------
il = (R/'identity-lock.md').read_text()
data['locks'] = []
for m in re.finditer(r'\*\*(Tingkat \d+ — \w+)\.\*\*(.*?)\n\n> (.*?)\n\n', il, re.S):
    body = ' '.join(l.lstrip('> ').strip() for l in m.group(3).split('\n'))
    data['locks'].append({'code': m.group(1), 'desc': m.group(2).strip().rstrip(':'),
                          'prompt': body.strip(), 'group': 'Identity lock'})
# standard lock
sm = re.search(r'## Lock standar.*?\n\n> (.*?)\n\n', il, re.S)
if sm:
    data['locks'].insert(0, {'code': 'Lock standar', 'desc': 'Pakai ini kalau ragu.',
        'prompt': ' '.join(l.lstrip('> ').strip() for l in sm.group(1).split('\n')).strip(),
        'group': 'Identity lock'})

# ---- larangan bullets ------------------------------------------------
data['bans'] = []
ban_sec = re.search(r'## Blok larangan(.*?)\n## ', il, re.S).group(1)
cur = ''
for line in ban_sec.split('\n'):
    hm = re.match(r'\*\*(.+?)\s*\(?.*?\)?:\*\*', line.strip())
    if hm: cur = hm.group(1).strip(); continue
    bm = re.match(r'- `(.+)`', line.strip())
    if bm: data['bans'].append({'group': cur, 'prompt': bm.group(1).strip()})

for k, v in data.items():
    print(f'{k:10s} {len(v)} entri')
pathlib.Path('/tmp/claude-0/-home-user-chromium/5718da5e-e7ac-59de-9275-7bf646dc8103/scratchpad/corpus.json').write_text(json.dumps(data, ensure_ascii=False))
