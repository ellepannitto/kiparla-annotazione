import pyconll

# Input and output file paths
conllu_path = 'PBB004.conllu'   # Replace with your input file path
tsv_path = 'PBB004.tsv'            # Desired output file

def format_feats(feats):
	"""
	Convert feats dictionary with set values to CoNLL-U formatted string.
	"""
	if not feats:
		return '_'
	return '|'.join(f"{k}={','.join(sorted(v))}" for k, v in sorted(feats.items()))

# Load the CoNLL-U file
sentences = pyconll.load_from_file(conllu_path)

# Open output TSV
with open(tsv_path, 'w', encoding='utf-8') as out_file:
	out_file.write("TID\tFORM\tLEMMA\tPOS\tFEATS\n")

	for sent in sentences:
		for token in sent:
			form = token.form or '_'
			lemma = token.lemma or '_'
			upos = token.upos or '_'
			feats = format_feats(token.feats)
			misc = token.misc or {}

			# Extract TID from MISC
			tid = misc.get('TID', None)

			if not tid:
				tid = "_"
			tid = "".join(tid)

			out_file.write(f"{tid}\t{form}\t{lemma}\t{upos}\t{feats}\n")