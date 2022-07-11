import json

with open("paper-author-map.json",'r',encoding='utf-8') as handle:
    p_data = json.load(handle)

with open("lunr-index.json",'r') as lunr_handle:
    exist_data = json.load(lunr_handle)
'''
with open("substrate-geo-map.json",'r') as handle:
    s_data = json.load(handle)

with open("paper-geo-map.json",'r') as handle:
    p_data = json.load(handle)

with open("organism-geo-map.json",'r') as handle: 
    o_data = json.load(handle)

with open("lunr-index.json",'r') as lunr_handle:
    exist_data = json.load(lunr_handle)

count = len(exist_data)
for idx,datum in enumerate(o_data):
    datum["idx"] = idx + count
    datum["from"] = datum.pop("GSE_id")
    datum["to"] = datum.pop("Organism")
    datum["fromClass"] = "GSE_ids"
    datum["toClass"] = "organisms"
    exist_data.append(datum)

count = len(exist_data)    
for idx,datum in enumerate(s_data):
    datum["idx"] = idx + count
    datum["from"] = datum.pop("GSE_id")
    datum["to"] = datum.pop("substrate")
    datum["fromClass"] = "GSE_ids"
    datum["toClass"] = "substrates"
    exist_data.append(datum)

count = len(exist_data)
for idx,datum in enumerate(p_data):
    datum["idx"] = idx + count
    datum["from"] = datum.pop("GSE_id")
    datum["to"] = datum.pop("pubmed_id")
    datum["fromClass"] = "GSE_ids"
    datum["toClass"] = "pubmeds"
    exist_data.append(datum)
'''

count = len(exist_data)
for idx,datum in enumerate(p_data):
    datum["idx"] = idx + count
    datum["from"] = datum.pop("author")
    datum["to"] = datum.pop("pubmed_id")
    datum["fromClass"] = "authors"
    datum["toClass"] = "pubmeds"
    exist_data.append(datum)



with open("lunr-index.json",'w') as writer:
    writer.write("indexed_data = '" + json.dumps(exist_data) + "';")
