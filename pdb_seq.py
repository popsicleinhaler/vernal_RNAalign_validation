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
import numpy as np
from Bio.PDB.QCPSuperimposer import QCPSuperimposer
import time
import random
import matplotlib.pyplot as plt
from spyrmsd import rmsd
from qcp_rmsd import *
import itertools
from numpy import random


def extract(structure, chain_id, residues, filename , model=0):
    """Write out selected portion to filename."""
    sel = ChainSelector(chain_id, model, residues)
    io = PDBIO()
    io.set_structure(structure)
    io.save(filename, sel)
    
#make it all into a list
# motif_residue_list
motif5 = [('5ib8.nx', ('14', 2827)), ('5ib8.nx', ('14', 2828)), ('5ib8.nx', ('14', 2829)), 
            ('5ib8.nx', ('14', 2840)), ('5ib8.nx', ('14', 2841))]

def getid(motif_component):
    return motif_component[0].split('.')[0]

def getresidue(motif_component):
    return motif_component[1][1]

def getchain(motif_component):
    return motif_component[1][0]

def parse_motif(motif):
    """returns a list [id chain , [residues]]"""
    residues = []
    for c in motif:
        residues.append(getresidue(c))
    return [getid(motif[0]), getchain(motif[0]), residues]

def bfs_expand(G, initial_nodes, nc_block=False, depth=1):
    """
        Extend motif graph starting with motif_nodes.
        Returns list of nodes.
    """
    total_nodes = [list(initial_nodes)]
    for d in range(depth):
        depth_ring = []
        e_labels = set()
        for n in total_nodes[d]:
            for nei in G.neighbors(n):
                depth_ring.append(nei)
                e_labels.add(G[n][nei]['label'])
        if e_labels.issubset({'CWW', 'B53', ''}) and nc_block:
            break
        else:
            total_nodes.append(depth_ring)
        # total_nodes.append(depth_ring)
    return set(itertools.chain(*total_nodes))

def parse_motif_nx(motif):
    """returns a list [id chain , [residues]]"""
    g = nx.read_gpickle('data/graphs/rna_graphs_nr/'+ getid(motif[0])+'.nx')
    residues=[]
    for c in motif: 
        c=(c[0],tuple(c[1]))
        residues.append(c)
    residues = bfs_expand(g,residues) 
    res =[]
    for n,d in g.nodes.items():
        for c in residues:
            if n == c:
                res.append(int(d['pdb_pos']))
    return [getid(motif[0]), getchain(motif[0]), res]

# motif = gkm(8001)['instance1']
# g = nx.read_gpickle(os.path.join(os.getcwd(),'data/graphs/rna_graphs_nr/'+ getid(motif[0])+'.nx'))
# print(g)
# pos = nx.circular_layout(g)
# nx.draw(g,gsubpos)
# plt.savefig('graph of 8001.png')
# plt.show()

# print(len(pos))
# gsubpos = dict(list(pos.items())[len(pos)//10:])
# print(gsubpos[('4v8n.nx', ('AA', 1))])
# print(len(gsubpos))
# gg = g.subgraph(range(100))
# posg = nx.circular_layout(gg)
# print(getid(motif[0]))
# nx.draw(g,gsubpos)
# plt.savefig('graph of 8001.png')
# plt.show()

def get_substructure(motif, new_dir, x, cif=True):
    #model = 'RNA'
    iD, chainn , residues = parse_motif_nx(motif) #use _nx or not actually they are the same NOT 6786 of the total are different

    class motifChain(Select):
        def accept_chain(self,chain):
            return chain.get_id() == chainn
    
    class motifResidues(Select):
        def accept_residue(self, res):
            return res.id[1] in residues #retuns True if residue is in motif

    class ChainSelector(Select): #(Select) why not?
        """Only accepts residues with right chainid, between start and end.
        Remove hydrogens, waters and ligands. Only use model 0 by default.
        """

        def __init__(self, chain_id, residues, model_id=0):
            """Initialize the class."""
            self.chain_id = chain_id
            self.model_id = model_id

        def accept_model(self, model):
            """Verify if model match the model identifier."""
            # model - only keep model 0
            if model.get_id() == self.model_id:
                return True
            return 0

        def accept_chain(self, chain):
            """Verify if chain match chain identifier."""
            #print(chain.get_id())
            if chain.get_id() == self.chain_id:
                return True
            return 0

        def accept_residue(self, residue):
            """Verify if a residue sequence is between the start and end sequence."""
            # residue - between start and end
            hetatm_flag, resseq, icode = residue.get_id()
            if hetatm_flag != " ":
                # skip HETATMS
                return 0
            if icode != " ":
                warnings.warn(
                    f"WARNING: Icode {icode} at position {resseq}", BiopythonWarning
                )
            if resseq in residues:
                # print('working?')
                return True
            return 0
        # is this necessary????????????????????????????
        def accept_atom(self, atom):
            """Verify if atoms are not Hydrogen."""
        #     # atoms - get rid of hydrogens
            name = atom.get_id()
        #     if _hydrogen.match(name):
            return True
        #     else:
        #         return True

    if cif:
        pc = MMCIFParser(QUIET=True)
        #with open('data/all_rna_pdb_nr/'+iD+'.cif', 'rb') as ref:
        structure = pc.get_structure(iD, os.path.join(os.getcwd(),'data/all_rna_pdb_nr/'+iD+'.cif'))
         #might not work
        sel = ChainSelector(chainn, residues , model_id=0)
        io = MMCIFIO()
        io.set_structure(structure)
        out = os.path.join(os.getcwd(),'cifs','instance_cifs', new_dir, iD+x+".cif")
        io.save(out, select=sel) #sel #motifResidues()
    else:
        pd = PDBParser(QUIET=True)
        pc = MMCIFParser(QUIET=True)
        pdbl = PDBList()

        pdbl.retrieve_pdb_file(iD, pdir = os.path.join(os.getcwd(),'pdbs/full'), file_format = 'mmCif') 
        structure = pc.get_structure(iD, os.path.join(os.getcwd(),'pdbs/full/'+iD+".cif"))
        out = os.path.join(os.getcwd(),'pdbs/'+iD+x+".pdb")
        
        sel = ChainSelector(chainn, residues, model_id=0)
        io = PDBIO()
        io.set_structure(structure)
        io.save(out, sel)
    return out
    # print('structure has:'+str(len(structure))+'-many models of which we chose the first!')
    # for r in list(structure[0][chainn].get_residues()):
    #     print(r.id[1], 'is it in this:', residues, 'or in this?', parse_motif(motif)[2])
    # reses = []
    # for r in list(structure[0][chainn].get_residues()):
    #     reses.append(r.id[1])
    

            #residue atts:['__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_generate_full_id', '_id', '_reset_full_id', 'add', 'child_dict', 'child_list', 'copy', 'detach_child', 'detach_parent', 'disordered', 'flag_disordered', 'full_id', 'get_atom', 'get_atoms', 'get_full_id', 'get_id', 'get_iterator', 'get_level', 'get_list', 'get_parent', 'get_resname', 'get_segid', 'get_unpacked_list', 'has_id', 'id', 'insert', 'internal_coord', 'is_disordered', 'level', 'parent', 'resname', 'segid', 'set_parent', 'sort', 'transform', 'xtra']
            #structure atts : ['__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_generate_full_id', '_id', '_reset_full_id', 'add', 'atom_to_internal_coordinates', 'child_dict', 'child_list', 'copy', 'detach_child', 'detach_parent', 'full_id', 'get_atoms', 'get_chains', 'get_full_id', 'get_id', 'get_iterator', 'get_level', 'get_list', 'get_models', 'get_parent', 'get_residues', 'has_id', 'header', 'id', 'insert', 'internal_to_atom_coordinates', 'level', 'parent', 'set_parent', 'transform', 'xtra'] 



    # for model in structure:
    #     print(model)
    #     for chain in model:
    #         print(chain)
    #         # for residue in chain:
    #         #     print(residue)

    # for model in structure:
    #     print(model)
    #     for chain in model:
    #         if chain == chainn:
    #             for residue in chain:
    #                 if residue in residues:
    #                     print(residue)
    #                     for atom in residue:
    #                         print(atom)
                    #for atom in residue:
                        #print(atom)    

                                                                                                                            #get_substructure(gkm(8001)['instance1'],'gaytest')
    #GET THE SUBSET OF THE STRUCTURE WITH RESIDUES FROM THE MOTIF
    #3400 had 6residues got error in the local RNAalign about missing attributes of atoms
    #in the server version got error that there are no residues 0
def fixer(filepath):
    cf = open(filepath,'r')
    cfl = cf.readlines()
    cf.close()
    out = os.path.join(filepath)
    print(out)
    #os.chdir('/Users/owner1/Sync/vernal-project/cifs/instance_cifs/fixed')
    fcf = open(out,'w')
    for l in cfl:
        if "''" in str(l):
            # bity = re.findall(r"'(.*?)'",l)[0]
            # bit = "'"+bitty+"''"
            # ls1 = l.replace(bit,'"'+bity+"'"+'"')
            ls1 = l.replace("'",'"',1).replace("''","'$",1).replace("$",'"')
            fcf.write(ls1)
        else:
            l2 = l.replace("\n"," \n")
            fcf.write(l2)
    fcf.close()

def run(i,N):
    print(gkm(i)['instance'+str(1)][0])
    print('Start')
    os.mkdir(os.path.join(os.getcwd(),'cifs','instance_cifs', str(i)+'_dir_'))
    out = os.path.join(os.getcwd(),'cifs','instance_cifs',str(i)+'_dir_','ins_list_'+str(i))
    print(os.getcwd())
    print(out)
    lis = open(out,'w')
    
    if N>200:
        eyes = random.randint(len(gkm(i)),size=200)
        for n in tqdm(eyes):
            n=n+1
            try:
                out = get_substructure(gkm(i)['instance'+str(n)], str(i)+'_dir_','_'+str(i)+'_instance'+str(n)+'_',cif=True)
                fixer(out)
                lis.write(out.split('/')[-1]+'\n')
            except ValueError:
                continue
    elif N<=200:
        for n in tqdm(range(1,N+1)):
            try:
                out = get_substructure(gkm(i)['instance'+str(n)], str(i)+'_dir_','_'+str(i)+'_instance'+str(n)+'_',cif=True)
                fixer(out)
                lis.write(out.split('/')[-1]+'\n')
            except ValueError:
                continue
        # except KeyError:
        #     break
    
        #print(n)
    print('Done')
    
for i in tqdm(range(3780,3880)):
    print('starting 6-motif: ',i)
    run(i,len(gkm(i)))


def get_residue_list(motif,nx=True):
    #model = 'RNA'
    if nx:
        iD, chainn , residues = parse_motif_nx(motif)
    else:
        iD, chainn , residues = parse_motif(motif)
    pc = MMCIFParser(QUIET=True)
    atom_list = []
    structure = pc.get_structure(iD, os.path.join(os.getcwd(),'data/all_rna_pdb_nr/'+iD+'.cif'))
    for residue in structure[0][chainn].get_residues():
        if residue.id[1] in residues:
            #print(residue)
            #print('working')
            for atom in residue.get_atoms():
                name = atom.get_name()
                #print(name)
                if name != 'H':
                    atom_list.extend(list(residue.get_atoms()))
    return atom_list

def superimpose_motif(fixed,moving):
    sup = Superimposer()
    # Specify the atom lists
    # 'fixed' and 'moving' are lists of Atom objects
    # The moving atoms will be put on the fixed atoms
    sup.set_atoms(fixed, moving)
    # Print rotation/translation/rmsd
    # print(sup.rotran)
    # print(sup.rms)
    # Apply rotation/translation to the moving atoms
    sup.apply(moving)
    rmsd = sup.rms
    return rmsd

def superimpose_motif_2(fixed, moving):
    sup = QCPSuperimposer()
    sup.set(fixed,moving)
    sup.get_init_rms()
    q = sup.get_rms()
    return q

def superimpose_motif_3(fixed, moving):
    return rmsd.rmsd(np.asarray(fixed),np.asarray(moving),np.asarray(range(len(fixed))),np.asarray(range(len(moving))),center=True,minimize=True)

def getCord(atom_list, arr=True):
    cs = []
    for a in atom_list:
        c = a.get_coord()
        cs.append(c)
    y=np.array([np.array(xi) for xi in cs])
    if arr:
        return y
    else:
        return cs


#### should find clusters that are similar enough in that they have the same number of atoms
def filter_size():
    sam ={}
    for i in tqdm(range(7900,8400)):
        try:
            c = len(get_residue_list(gkm(i)['instance1']))
        except ValueError:
            continue
        sam[i] = c
        print(i, c)
    cfile = open('/Users/owner1/Sync/vernal-project/atomlist7900to8400forins1n10.pkl', "wb")
    pickle.dump(sam, cfile)
    cfile.close()
    pass

def sn(i):
    rnd = random.sample(range(1,len(gkm(i))),20)
    szs = {'nx':[],'not':[]}
    for k in tqdm(rnd):
        # sz = len(get_residue_list(gkm(i)['instance'+str(k)]))
        # szs['not'].append(sz)
        try:
            eh = len(get_residue_list(gkm(i)['instance'+str(k)],nx=False))
        except ValueError:
            continue
        szs['nx'].append(eh)
    return szs
#want to see the similar set of motifs to 7991 8001 8028
# 151 7991 7977 7955 7924 8046 8071 8092      8154
# 156 8001 7970 7914 8003 8011 8019 8047 8074 8103
# 149 8028 8017 7988 7902 8065 8091 8104 8149 8223 8110
#check length of atoms in the remainder of instances not just the first
# find the one with low instance count and run just he self in the new index and then the cross
# i=8001
# i2=8003
# start2=time.time()
# # r=superimpose_motif_2(getCord(get_residue_list(gkm(i)['instance8']),arr=False),getCord(get_residue_list(gkm(i2)['instance16']),arr=False))
# # print(r)

# fixed = getCord(get_residue_list(gkm(i)['instance8']))
# moving = getCord(get_residue_list(gkm(i2)['instance16']))
# end2=time.time()
# print('second',end2-start2)
# start1 = time.time()
# r = rmsd_qcp(fixed,moving)
# print(r)
# end1 = time.time()
# print('first',end1-start1)

# start3=time.time()
# r=superimpose_motif_3(fixed,moving)
# print(r)
# end3=time.time()
# print('third',end3-start3)



# i=8000
# n=1
#print('motif list is this:', get_residue_list(gkm(i)['instance'+str(n)]), 'and the attributes of a compoennt are:',dir(get_residue_list(gkm(i)['instance'+str(n)])[0]))

#superimpose_motif(get_residue_list(gkm(i)['instance'+str(n)]),get_residue_list(gkm(i)['instance'+str(n+1)]))


# pair = set()
# for a in range(1,num_instances+1):
#     for b in range(1,num_instances+1):
#         if a == b:
#             pair.add((a,b))#accounts for same same control
#         else:
#             pair.add(frozenset({a,b}))
# pairs=[]
# for p in list(pair):
#     pairs.append(list(p))

# i1 = 8103 #must run the cross interaction
# i2 = 8003

def intracluster_similarity():
    

    for i in [7991]:
        print('intracluster',i)
        e1=0
        if i==8003:
            div=9
        else:
            div=5
        div=1
        num_instances = int(len(gkm(i))/div)        
        pairs=[]
        for a in range(1,num_instances+1):
            for b in range(1, a+1):
                pairs.append([a,b])
        all_2_all = np.zeros((num_instances+1,num_instances+1))
        for x,y in tqdm(pairs):
            try:
                fixed = getCord(get_residue_list(gkm(i)['instance'+str(x)],nx=False))
                moving = getCord(get_residue_list(gkm(i)['instance'+str(y)],nx=False))
                resize=min([np.shape(fixed)[0],np.shape(moving)[0]])
                fixed=fixed[:resize]
                moving=moving[:resize]
                all_2_all[x,y]=superimpose_motif_2(fixed,moving)
            except ValueError:
                e1 += 1
                continue
        print('The number of value errors is: ',e1)
        a_file = open("data_self_"+str(i)+".pkl", "wb")
        pickle.dump(all_2_all, a_file)
        a_file.close()
################################################################################################################
def intercluster_similarity():
    i1=7991
    i2=8103
    for i1,i2 in [[7991,8001] ]:
        print('intercluster',i1,i2)
        if i2==8154:
            div=10
        else:
            div=5
        div=1
        frame_2 = {}
        z_instances = int(len(gkm(i1))/div)
        o_instances = int(len(gkm(i2))/div)
        e2 = 0
        # if z_instances>o_instances:
        #     bt = np.ones((z_instances+1,o_instances+1))
        #     bt = np.tril(bt)
        #     pairs=[]
        #     for a in range(1,z_instances+1):
        #          for b in range(1,o_instances+1):
        #             pairs.append([a,b])
        # else:
        #     bt = np.ones((o_instances+1,z_instances+1))
        #     bt = np.tril(bt)
        #     pairs=[]
        #     for a in range(1,o_instances+1):
        #          for b in range(1,z_instances+1):
        #             pairs.append([a,b])
        bt = np.zeros((z_instances+1,o_instances+1))
        pairs=[]        
        for a in range(1,z_instances+1):
             for b in range(1,o_instances+1):
                pairs.append([a,b])

        for x,y in tqdm(pairs): #order of x and y matter because associated to either 8000 or 8001
            #if bt[x,y] == 1:
            try:
                # if z_instances>o_instances:
                #     fixed = getCord(get_residue_list(gkm(i1)['instance'+str(x)],nx=True))
                #     moving = getCord(get_residue_list(gkm(i2)['instance'+str(y)],nx=True))
                # else:
                #     fixed = getCord(get_residue_list(gkm(i1)['instance'+str(y)],nx=True))
                #     moving = getCord(get_residue_list(gkm(i2)['instance'+str(x)],nx=True))
                fixed = getCord(get_residue_list(gkm(i1)['instance'+str(x)]))
                moving = getCord(get_residue_list(gkm(i2)['instance'+str(y)]))
                resize=min([np.shape(fixed)[0],np.shape(moving)[0]])
                fixed=fixed[:resize]
                moving=moving[:resize]
                bt[x,y]=superimpose_motif_3(fixed,moving)
            except ValueError:
                e2 += 1
                continue
        frame_2['bt_smthn']=[bt,e2]

        b_file = open("data3_inter_"+str(i1)+'n'+str(i2)+".pkl", "wb")
        pickle.dump(frame_2, b_file)
        b_file.close()
##########################################################################################################################################
# for k in range(1,166+1):
#     if len(get_residue_list(gkm(i)['instance'+str(n)])) == len(get_residue_list(gkm(i)['instance'+str(n+k)])):
#         superimpose_motif(get_residue_list(gkm(i)['instance'+str(n)]),get_residue_list(gkm(i)['instance'+str(n+k)]))

# print('different cluster')

# for i in range(8000,8005):
#     if len(get_residue_list(gkm(8000)['instance'+str(n)])) == len(get_residue_list(gkm(i)['instance'+str(n)])):
#         superimpose_motif(get_residue_list(gkm(8000)['instance'+str(n)]),get_residue_list(gkm(i)['instance'+str(n)])) 
empty_motifs = []
sections = {}
for i in tqdm(range(2,9404)):
    try:
        p = len(gkm(i-1)['instance1'])
        n = len(gkm(i)['instance1'])
    except KeyError:
        empty_motifs.append(i)
        continue
    if p != n:
        sections[i] = n



# full={'_atom_site.group_PDB'
# , '_atom_site.id'
# , '_atom_site.type_symbol'
# , '_atom_site.label_atom_id'
# , '_atom_site.label_alt_id'
# , '_atom_site.label_comp_id'
# , '_atom_site.label_asym_id'
# , '_atom_site.label_entity_id'
# , '_atom_site.label_seq_id'
# , '_atom_site.pdbx_PDB_ins_code'
# , '_atom_site.Cartn_x'
# , '_atom_site.Cartn_y'
# , '_atom_site.Cartn_z'
# , '_atom_site.occupancy'
# , '_atom_site.B_iso_or_equiv'
# , '_atom_site.pdbx_formal_charge'
# , '_atom_site.auth_seq_id'
# , '_atom_site.auth_comp_id'
# , '_atom_site.auth_asym_id'
# , '_atom_site.auth_atom_id'
# , '_atom_site.pdbx_PDB_model_num'}

# suby={'_atom_site.group_PDB'
# , '_atom_site.id'
# , '_atom_site.type_symbol'
# , '_atom_site.label_atom_id'
# , '_atom_site.label_alt_id'
# , '_atom_site.label_comp_id'
# , '_atom_site.label_asym_id'
# , '_atom_site.label_entity_id'
# , '_atom_site.label_seq_id'
# , '_atom_site.pdbx_PDB_ins_code'
# , '_atom_site.Cartn_x'
# , '_atom_site.Cartn_y'
# , '_atom_site.Cartn_z'
# , '_atom_site.occupancy'
# , '_atom_site.B_iso_or_equiv'
# , '_atom_site.auth_seq_id'
# , '_atom_site.auth_asym_id'
# , '_atom_site.pdbx_PDB_model_num'}







# ATOM      1  O5'   C X  13       0.047  -6.959   1.489  1.00 65.39           O  
# ATOM      2  C5'   C X  13       1.106  -6.846   0.528  1.00 66.02           C  
# ATOM      3  C4'   C X  13       0.659  -6.175  -0.764  1.00 66.28           C  
# ATOM      4  O4'   C X  13      -0.185  -5.025  -0.477  1.00 65.99           O  
# ATOM      5  C3'   C X  13       1.790  -5.592  -1.602  1.00 67.11           C  
# ATOM      6  O3'   C X  13       2.408  -6.569  -2.438  1.00 68.74           O  
# ATOM      7  C2'   C X  13       1.053  -4.538  -2.419  1.00 66.09           C  
# ATOM      8  O2'   C X  13       0.297  -5.090  -3.484  1.00 65.49           O  
# ATOM      9  C1'   C X  13       0.134  -3.945  -1.350  1.00 65.21           C  
# ATOM     10  N1    C X  13       0.664  -2.744  -0.554  1.00 64.39           N  
# ATOM     11  C2    C X  13       1.173  -1.572  -1.181  1.00 64.55           C  
# ATOM     12  O2    C X  13       1.225  -1.466  -2.414  1.00 64.48           O  
# ATOM     13  N3    C X  13       1.621  -0.542  -0.411  1.00 63.83           N  
# ATOM     14  C4    C X  13       1.579  -0.640   0.920  1.00 64.21           C  
# ATOM     15  N4    C X  13       2.037   0.392   1.629  1.00 64.00           N  
# ATOM     16  C5    C X  13       1.068  -1.804   1.581  1.00 64.11           C  
# ATOM     17  C6    C X  13       0.626  -2.809   0.815  1.00 63.57           C  
# ATOM     18  P     G X  14       3.969  -6.891  -2.298  1.00 71.18           P  
# ATOM     19  OP1   G X  14       4.095  -8.366  -2.274  1.00 71.44           O  
# ATOM     20  OP2   G X  14       4.527  -6.124  -1.162  1.00 71.77           O  
# ATOM     21  O5'   G X  14       4.641  -6.376  -3.658  1.00 70.77           O  
# ATOM     22  C5'   G X  14       3.901  -5.727  -4.687  1.00 70.87           C  
# ATOM     23  C4'   G X  14       4.548  -4.424  -5.137  1.00 70.84           C  
# ATOM     24  O4'   G X  14       3.796  -3.293  -4.618  1.00 70.61           O  
# ATOM     25  C3'   G X  14       5.976  -4.156  -4.668  1.00 71.14           C  
# ATOM     26  O3'   G X  14       6.950  -4.864  -5.448  1.00 71.50           O  


# ATOM 1   P P     . G A ? 1 ? -94.379 -36.136 28.829  1.0 41.18 2436 BA 1 
# ATOM 2   O OP1   . G A ? 1 ? -95.531 -35.874 27.972  1.0 42.55 2436 BA 1 
# ATOM 3   O OP2   . G A ? 1 ? -93.998 -37.522 29.132  1.0 42.62 2436 BA 1 
# ATOM 4   O 'O5'' . G A ? 1 ? -93.130 -35.418 28.171  1.0 41.09 2436 BA 1 
# ATOM 5   C 'C5'' . G A ? 1 ? -92.260 -36.114 27.269  1.0 40.44 2436 BA 1 
# ATOM 6   C 'C4'' . G A ? 1 ? -91.184 -35.182 26.806  1.0 38.65 2436 BA 1 
# ATOM 7   O 'O4'' . G A ? 1 ? -90.428 -34.738 27.954  1.0 37.88 2436 BA 1 
# ATOM 8   C 'C3'' . G A ? 1 ? -90.149 -35.764 25.873  1.0 38.17 2436 BA 1 
# ATOM 9   O 'O3'' . G A ? 1 ? -90.588 -35.740 24.533  1.0 39.02 2436 BA 1 
# ATOM 10  C 'C2'' . G A ? 1 ? -88.974 -34.833 26.095  1.0 38.34 2436 BA 1 
# ATOM 11  O 'O2'' . G A ? 1 ? -89.160 -33.612 25.398  1.0 38.42 2436 BA 1 
# ATOM 12  C 'C1'' . G A ? 1 ? -89.069 -34.588 27.600  1.0 36.87 2436 BA 1 
# ATOM 13  N N9    . G A ? 1 ? -88.292 -35.550 28.379  1.0 39.94 2436 BA 1 
# ATOM 14  C C8    . G A ? 1 ? -88.763 -36.437 29.315  1.0 38.63 2436 BA 1 
# ATOM 15  N N7    . G A ? 1 ? -87.826 -37.169 29.841  1.0 37.24 2436 BA 1 
# ATOM 16  C C5    . G A ? 1 ? -86.668 -36.735 29.217  1.0 36.96 2436 BA 1 
# ATOM 17  C C6    . G A ? 1 ? -85.336 -37.159 29.375  1.0 37.3  2436 BA 1 
# ATOM 18  O O6    . G A ? 1 ? -84.884 -38.043 30.138  1.0 37.52 2436 BA 1 
# ATOM 19  N N1    . G A ? 1 ? -84.483 -36.458 28.530  1.0 35.82 2436 BA 1 
# ATOM 20  C C2    . G A ? 1 ? -84.871 -35.488 27.650  1.0 33.61 2436 BA 1 
# ATOM 21  N N2    . G A ? 1 ? -83.915 -34.936 26.906  1.0 32.63 2436 BA 1 
# ATOM 22  N N3    . G A ? 1 ? -86.102 -35.089 27.503  1.0 33.57 2436 BA 1 
# ATOM 23  C C4    . G A ? 1 ? -86.943 -35.744 28.311  1.0 37.13 2436 BA 1 
# ATOM 24  P P     . U A ? 2 ? -90.282 -36.994 23.585  1.0 46.94 2437 BA 1 
# ATOM 25  O OP1   . U A ? 2 ? -90.969 -36.681 22.312  1.0 48.89 2437 BA 1 
# ATOM 26  O OP2   . U A ? 2 ? -90.605 -38.254 24.304  1.0 47.13 2437 BA 1 
# ATOM 27  O 'O5'' . U A ? 2 ? -88.711 -36.916 23.361  1.0 38.14 2437 BA 1 
# ATOM 28  C 'C5'' . U A ? 2 ? -88.161 -35.854 22.587  1.0 39.43 2437 BA 1 
# ATOM 29  C 'C4'' . U A ? 2 ? -86.665 -35.942 22.574  1.0 40.2  2437 BA 1 
# ATOM 30  O 'O4'' . U A ? 2 ? -86.185 -35.841 23.937  1.0 40.88 2437 BA 1 
# ATOM 31  C 'C3'' . U A ? 2 ? -86.067 -37.245 22.088  1.0 40.62 2437 BA 1 
# ATOM 32  O 'O3'' . U A ? 2 ? -86.018 -37.372 20.676  1.0 41.31 2437 BA 1 
# ATOM 33  C 'C2'' . U A ? 2 ? -84.692 -37.209 22.731  1.0 41.35 2437 BA 1 