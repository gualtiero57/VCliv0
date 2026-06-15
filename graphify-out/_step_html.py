import json
from pathlib import Path
from graphify.build import build_from_json
from graphify.export import to_html

extraction = json.loads(Path('graphify-out/.graphify_extract.json').read_text(encoding='utf-8'))
analysis = json.loads(Path('graphify-out/.graphify_analysis.json').read_text(encoding='utf-8'))
labels_path = Path('graphify-out/.graphify_labels.json')
community_labels = json.loads(labels_path.read_text(encoding='utf-8')) if labels_path.exists() else {}
community_labels_int = {int(k): v for k, v in community_labels.items()}

G = build_from_json(extraction)
communities = {int(k): v for k, v in analysis['communities'].items()}

to_html(G, communities, 'graphify-out/', community_labels=community_labels_int)
print('HTML generated at graphify-out/graph.html')
