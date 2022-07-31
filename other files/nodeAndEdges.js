const geo_substrate = JSON.parse(geo_substrate_map);
const geo_organism = JSON.parse(geo_organism_map);
const geo_paper = JSON.parse(geo_paper_map);
const paper_author = JSON.parse(author_paper_map);
var old_pubids = [];

network_elements = [{ data: { id: 'glucose'}, classes: 'substrates' }, { data: { id: 'xylose'}, classes: 'substrates' }, { data: { id: 'cellulose'}, classes: 'substrates' }, { data: { id: 'carbon'}, classes: 'substrates' }, { data: { id: 'avicel'}, classes: 'substrates' }];
for (let i=0; i < geo_substrate.length; i++)
{
	var node = { data: { id: geo_substrate[i]['GSE_id']}, classes: 'GSE_ids' };
	var edge = { data: { id: geo_substrate[i]['GSE_id'] + '-' + geo_substrate[i]['substrate'], source:geo_substrate[i]['GSE_id'] ,target: geo_substrate[i]['substrate'] } }
	network_elements.push(node);
	network_elements.push(edge);
}
for (let i=0; i < geo_organism.length; i++)
{
	var node = { data: { id: geo_organism[i]['Organism']}, classes: 'organisms' };
	var edge = { data: { id: geo_organism[i]['GSE_id'] + '-' + geo_organism[i]['Organism'], source:geo_organism[i]['GSE_id'] ,target: geo_organism[i]['Organism'] } }
	network_elements.push(node);
	network_elements.push(edge);
}

for (let i=0; i < geo_paper.length; i++)
{
	if(geo_paper[i]['pubmed_id'] != '') {
		var node = { data: {id: geo_paper[i]['pubmed_id']}, classes: 'pubmeds'};
		var edge = { data: { id: geo_paper[i]['GSE_id'] + '-' + geo_paper[i]['pubmed_id'], source: geo_paper[i]['GSE_id'], target: geo_paper[i]['pubmed_id'] } }
		old_pubids.push(geo_paper[i]['pubmed_id'])
		network_elements.push(node);
		network_elements.push(edge);
	}
}
/*
for (let i=0; i < paper_author.length; i++)
{
	var node = { data: {id: paper_author[i]['author']}, classes: 'authors'};
	network_elements.push(node);

	if(!(paper_author[i]['pubmed_id'] in old_pubids))
	{
		var node = { data: {id: paper_author[i]['pubmed_id']}, classes: 'pubmeds'};
		network_elements.push(node);
	}

	var edge = { data: { id: paper_author[i]['author'] + '-' + paper_author[i]['pubmed_id'], source: paper_author[i]['author'], target: paper_author[i]['pubmed_id'] } };
	network_elements.push(edge);
}
*/