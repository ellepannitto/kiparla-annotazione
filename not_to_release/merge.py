import csv

# File paths
linguistic_path = 'lemmas/BOD2018.tsv'
rich_path = '/Users/ludovica/Documents/projects/KIParla/KIP_parsed/BOD2018.vert.tsv'
output_path = 'BOD2018.merged.tsv'

# Step 1: Load linguistic.tsv into a dictionary using TID as key
linguistic_data = {}
with open(linguistic_path, encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        tid = row['TID']
        linguistic_data[tid] = {
            'LING_FORM': row['FORM'],
            'LING_LEMMA': row['LEMMA'],
            'LING_POS': row['POS'],
            'LING_FEATS': row['FEATS']
        }

# Step 2: Open rich.tsv and write enriched version
with open(rich_path, encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8', newline='') as outfile:
    reader = csv.DictReader(infile, delimiter='\t')
    # New columns to add
    new_fields = ['LING_FORM', 'LING_LEMMA', 'LING_POS', 'LING_FEATS']
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames + new_fields, delimiter='\t')
    writer.writeheader()

    for row in reader:
        tid = row['token_id']
        ling_info = linguistic_data.get(tid, {
            'LING_FORM': '_',
            'LING_LEMMA': '_',
            'LING_POS': '_',
            'LING_FEATS': '_'
        })
        row.update(ling_info)
        writer.writerow(row)
