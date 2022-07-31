from Bio import Entrez as en
import json
import re
from datetime import datetime

en.email = "122013059@sastra.ac.in"

org_names = ['Aspergillus fumigatus', 'Fusarium graminearum', 'Podospora comata', 'Pyricularia oryzae', 'Rhizoctonia solani AG-1 IA', 'Aspergillus oryzae', 'Botrytis cinerea', 'Coprinopsis cinerea', 'Cryptococcus gattii VGII R265', 'Ganoderma boninense', 'Gelatoporia subvermispora', 'Heterobasidion parviporum', 'Phanerodontia chrysosporium', 'Rhizophlyctis rosea', 'Scytalidium lignicola', 'Talaromyces marneffei', 'Talaromyces piceae', 'Thermothelomyces thermophilus', 'Trichoderma virens', 'Valsa mali', 'Volvariella volvacea']
print(len(org_names))

for org_name in org_names:
    # print(org_name)
    term = org_name.replace(" ", "_")

    queries = [
        # f'''("{org_name}"[MeSH Terms] OR "{org_name}"[Organism] OR {org_name}[All Fields]) AND ("glucose"[MeSH Terms] OR glucose[All Fields]) ''',
        # f'''("{org_name}"[MeSH Terms] OR "{org_name}"[Organism] OR {org_name}[All Fields]) AND ("cellulose"[MeSH Terms] OR cellulose[All Fields]) ''',
        # f'''("{org_name}"[MeSH Terms] OR "{org_name}"[Organism] OR {org_name}[All Fields]) AND ("cellulose"[MeSH Terms] OR avicel[All Fields]) ''',
        f'''("{org_name}"[MeSH Terms] OR "{org_name}"[Organism] OR {org_name}[All Fields]) AND ("xylose"[MeSH Terms] OR xylose[All Fields]) ''',
        # f'''("{org_name}"[MeSH Terms] OR "{org_name}"[Organism] OR {org_name}[All Fields]) AND ("carbon"[MeSH Terms] OR carbon[All Fields]) ''',
        ]

    metadata = []
    for query in queries:
        handle = en.esearch(db="gds", term=query, retmax=10000)
        result = en.read(handle)
        handle.close()

        print(query)
        print(len(result['IdList']), " hits \n")

        for ID in result['IdList']:
            handle2 = en.esummary(db="gds", id=ID, rettype='xml', retmode='text')
            details = en.read(handle2)[0]
            # print(details.keys())
            handle2.close()

            row = dict(organism=re.findall(r"\"\w+\s*\w*\"", query)[0].replace("\"", ""),
                       source=re.findall(r"\"\w+\s*\w*\"", query)[1].replace("\"", ""),
                       title=details['title'], Accession=details['Accession'], summary=details['summary'], keywords=query, pubmed=details['PubMedIds'])
            metadata.append(row)
            # break
            # Write metadata to a JSON file
            with open("metadata_" + term + '_xylose', "w") as file:
                json.dump(list(metadata), file)

print("\n\nSuccessfully completed !!")
print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
