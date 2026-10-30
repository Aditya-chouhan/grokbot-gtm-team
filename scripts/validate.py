import json,re
from pathlib import Path
r=Path(__file__).resolve().parents[1]
bots=json.loads((r/'team.json').read_text())['bots']
assert len(bots)==15
assert len({b['name'] for b in bots})==15
bundle=(r/'dist/grok-team-import.txt').read_text()
for b in bots:
 text=(r/'agents'/b['file']).read_text()
 assert 'TEAM OPERATING RULES' in text and text in bundle
for p in r.rglob('*.md'):
 for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if '://' not in link and not link.startswith('#'): assert (p.parent/link).exists(),(p,link)
print('Validated 15 self-contained Bots, bundle coverage, unique names and local links. Grok behavior not tested.')
