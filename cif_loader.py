import os
from Bio.PDB import *
from tqdm import tqdm

pc = MMCIFParser(QUIET=True)

cifspath = os.path.join(os.getcwd(),'data/all_rna_pdb_nr')
fullcifs = {}
for c in tqdm(os.listdir(cifspath)):
	iD = c.split('.')[0]
	try:
		fullcifs[iD] = pc.get_structure(iD, cifspath+'/'+c)
	except ValueError:
		continue