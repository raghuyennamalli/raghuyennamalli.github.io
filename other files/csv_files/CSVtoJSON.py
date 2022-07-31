import csv
import json

data_list = []

# for org in ['Aspergillus fumigatus','Aspergillus oryzae', 'Botrytis cinerea', 'Coprinopsis cinerea', 'Fusarium graminearum', 'Gelatoporia subvermispora', 'Phanerodontia chrysosporium', 'Pyricularia oryzae', 'Talaromyces marneffei', 'Thermothelomyces thermophilus', 'Trichoderma virens', 'Valsa mali', 'Volvariella volvacea']:
# 	with open("substrate-geo/" + org + "-substrate_for_geo.csv") as csv_handle:
# 		data = csv.DictReader(csv_handle)
# 		for row in data:
# 			data_list.append(row)
# print(data_list)
#


with open("author_from_paper.csv") as csv_handle:
    data = csv.DictReader(csv_handle)
    for row in data:
        data_list.append(row)

print(data_list)

with open("paper-author-map.json", 'w') as json_handle:
    json_handle.write("author_paper_map='" + json.dumps(data_list,ensure_ascii=False) + "';")
#
