import pandas as pd
import json

#artists = pd.read_json('csvjson.json')
#print(artists)

js = '''[
	{
	'name': 'John',
	'age': '32'
	},
	{'name': 'Maria',
	'age': '28'
	}
]'''

def ler_json(arq_json):
	with open(arq_json, 'r', encoding='utf-8') as f:
		json.load(f)
		
#artists = ler_json('csvjson.json')

print(json.dumps(js, indent=4, sort_keys = True))