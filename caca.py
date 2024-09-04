import json
with open('textos.json') as f:
    d = json.load(f)
    print(d.keys())