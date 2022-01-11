import networkx as nx
import pickle
from pdb_seq import getid, getchain



motif5 = [('5ib8.nx', ('14', 2827)), ('5ib8.nx', ('14', 2828)), ('5ib8.nx', ('14', 2829)), 
            ('5ib8.nx', ('14', 2840)), ('5ib8.nx', ('14', 2841))]

def parse_motif_nx(motif):
    """returns a list [id chain , [residues]]"""

    g = nx.read_gpickle('data/graphs/rna_graphs_nr/'+ getid(motif[0])+'.nx')

    residues=[]
    for n,d in g.nodes.items():
    	for c in motif:	
    		if n == c:
    			residues.append(d['pdb_pos'])

    return [getid(motif[0]), getchain(motif[0]), residues]

print(parse_motif_nx(motif5))