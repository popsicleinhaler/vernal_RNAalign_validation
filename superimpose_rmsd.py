from Bio.PDB import *
from Bio.PDB.MMCIF2Dict import MMCIF2Dict
from Bio.PDB.mmcifio import MMCIFIO
import networkx as nx
import pickle
from mgraphs_instances import *
from tqdm import tqdm
import os
from Bio import BiopythonWarning
import warnings
#from pdb_seq import *
from os import *


#test
#input 2 motifs cif files get rmsd
#know has 1 cahin only

#navigate to cifs folder

pc = MMCIFParser(QUIET=True)
mypath = os.path.join(os.getcwd(),'cifs')
res_lists = []
for f in os.listdir(mypath):
	path_f = os.path.join(mypath, f)
	filename, file_extension = os.path.splitext(path_f)
	if file_extension == '.cif':
		iD = filename.split('_')[0]
		structure = pc.get_structure(iD, path_f)
		res = []
		for model in structure.get_list():
			for chain in model.get_list():
				for residue in chain.get_list():
					res.append(residue)
		res_lists.append(res)

#QCPSuperimposer.QCPSuperimposer
fixed, moving = res_lists[0], res_lists[1]

sup = Superimposer()
# Specify the atom lists
# 'fixed' and 'moving' are lists of Atom objects
# The moving atoms will be put on the fixed atoms
sup.set_atoms(fixed, moving)
# Print rotation/translation/rmsd
print(sup.rotran)
print(sup.rms)
# Apply rotation/translation to the moving atoms
sup.apply(moving)
rmsd = sup.rmsd()
print(rmsd)
