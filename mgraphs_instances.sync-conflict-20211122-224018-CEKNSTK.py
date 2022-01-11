import pickle
import sys
from tqdm import tqdm


def get_motifs():
	pass

filem = open('results/mggs/my_metagraph.p', 'rb')
filema = open('results/mggs/my_magagraph.p', 'rb')

mmg = pickle.load(filem)
# print(mmg)
# print(dir(mmg))
# print('woah this is how many nodes in the pickle turned graph: ', len(mmg.graph.nodes()))
#MGraphAll object

mmaga = pickle.load(filema)
# print(mmaga)
# print(dir(mmaga))
# print('this is the lenght of maga : ', len(mmaga.nodes()))
#<networkx.classes.digraph.DiGraph object at 0x7fbc5e0f9730>
##### for maga_graph
# ['__class__', '__contains__', '__delattr__', '__dict__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', 
# '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', 
# '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
# '_adj', '_node', '_pred', '_succ', 'add_edge', 'add_edges_from', 'add_node', 
# 'add_nodes_from', 'add_weighted_edges_from', 'adj', 'adjacency', 
# 'adjlist_inner_dict_factory', 'adjlist_outer_dict_factory', 'clear', 'clear_edges', 
# 'copy', 'degree', 'edge_attr_dict_factory', 'edge_subgraph', 'edges', 'get_edge_data', 
# 'graph', 'graph_attr_dict_factory', 'has_edge', 'has_node', 'has_predecessor', 
# 'has_successor', 'in_degree', 'in_edges', 'is_directed', 'is_multigraph', 'name', 
# 'nbunch_iter', 'neighbors', 'node_attr_dict_factory', 'node_dict_factory', 'nodes', 
# 'number_of_edges', 'number_of_nodes', 'order', 'out_degree', 'out_edges', 'pred', 
# 'predecessors', 'remove_edge', 'remove_edges_from', 'remove_node', 'remove_nodes_from', 
# 'reverse', 'size', 'subgraph', 'succ', 'successors', 'to_directed', 'to_directed_class', 
# 'to_undirected', 'to_undirected_class', 'update']

# i=0
# for n in mmg.graph.edges():
# 	if i<10:
# 		print(n)

# 	i+=1



# mmaga.nodes[1]['node_set']
# mmaga.edges[1]['edge_set']

# i=0
# for n in mmaga.edges():
# 	# if i>110 and i<120:
# 	# 	print(n)
# 	# i+=1
# 	# print(n)
# 	pass

# print("GAagaysgyasgydgasdfgashfglajsfkjahsf:jkashflahskfjHkjashflkajhAFKJSHFAKSJHFALKSJFHSFG")

# for k,v in mmaga.nodes.items():
# 	print(k)


# for n in mmaga.nodes():
# 	if i<1:
# 		print(mmaga.nodes[n])
# 	i+=1


#pdbid, _ = .reversed_node_map[list(node_index)[0]]

# print(mmaga.nodes[list(mmaga.nodes())[0]]['node_set'])

# ss = {1116,1117,1118,1119,1120,1121}
# #mmaga.edges() didn;t work
# k=0
# while k <= len(mmaga.nodes())-1:
# 	for fs in mmaga.nodes[list(mmaga.nodes())[k]]['node_set']:
# 		# print('works')
# 		if ss.issubset(fs):
# 			print(m)
# 	k+=1
# #also doesn't find any

# # print(mmaga.nodes[list(mmaga.nodes())[0]]['node_set'])


# #closest ive ever been
# motif_list = []
# for i in range(119-1):
# 	motif = list(mmaga.nodes[list(mmaga.nodes())[1000]]['node_set'])[i]
# 	motif_list.append(motif)

# real_motif_list = []
# for m in motif_list:
# 	for i in m:
# 		real_motif_list.append(mmg.reversed_node_map[i])


# [('5ib8.nx', ('14', 2827)), ('5ib8.nx', ('14', 2828)), ('5ib8.nx', ('14', 2829)), 
# ('5ib8.nx', ('14', 2840)), ('5ib8.nx', ('14', 2841)), ('5lzd.nx', ('a', 1512)), 
# ('5lzd.nx', ('a', 1522)), ('5lzd.nx', ('a', 1523)), ('5lzd.nx', ('a', 1510)), 
# ('5lzd.nx', ('a', 1511)), ('5o60.nx', ('A', 2855)), ('5o60.nx', ('A', 2856)), 
# ('5o60.nx', ('A', 2857)), ('5o60.nx', ('A', 3010)), ('5o60.nx', ('A', 3011)), 
# ('3oxe.nx', ('A', 4)), ('3oxe.nx', ('A', 5)), ('3oxe.nx', ('A', 84)), 
# ('3oxe.nx', ('A', 85)), ('3oxe.nx', ('A', 3)), ('4xej.nx', ('B16S', 36)), 
# ('4xej.nx', ('B16S', 37)), ('4xej.nx', ('B16S', 38)), ('4xej.nx', ('B16S', 391)), 
# ('4xej.nx', ('B16S', 392)), ('4v8p.nx', ('H1', 299)), ('4v8p.nx', ('H1', 300)), 
# ('4v8p.nx', ('H1', 301)), ('4v8p.nx', ('H1', 313)), ('4v8p.nx', ('H1', 314)), ('4v9q.nx', 
# 	('CA', 2799)), ('4v9q.nx', ('CA', 2800)), ('4v9q.nx', ('CA', 2811)), ('4v9q.nx', ('CA', 2812)), 
# ('4v9q.nx', ('CA', 2813)), ('5ot7.nx', ('4', 724)), ('5ot7.nx', ('4', 837)), ('5ot7.nx', ('4', 838)), 
# ('5ot7.nx', ('4', 722)), ('5ot7.nx', ('4', 723)), ('3ndb.nx', ('M', 76)), ('3ndb.nx', ('M', 77)), 
# ('3ndb.nx', ('M', 99)), ('3ndb.nx', ('M', 100)), ('3ndb.nx', ('M', 101)), ('5lzd.nx', ('a', 1521)), 
# ('5lzd.nx', ('a', 1522)), ('5lzd.nx', ('a', 1523)), ('5lzd.nx', ('a', 1510)), ('5lzd.nx', ('a', 1511)), 
# ('4v6d.nx', ('DA', 2816)), ('4v6d.nx', ('DA', 2817)), ('4v6d.nx', ('DA', 2828)), ('4v6d.nx', ('DA', 2829)), 
# ('4v6d.nx', ('DA', 2830)), ('4v6d.nx', ('DA', 407)), ('4v6d.nx', ('DA', 408)), ('4v6d.nx', ('DA', 409)), 
# ('4v6d.nx', ('DA', 419)), ('4v6d.nx', ('DA', 420)), ('6frk.nx', ('5', 1484)), ('6frk.nx', ('5', 1485)), 
# ('6frk.nx', ('5', 1638)), ('6frk.nx', ('5', 1639)), ('6frk.nx', ('5', 1640)), ('4wq1.nx', ('14', 2275)), 
# ('4wq1.nx', ('14', 2276)), ('4wq1.nx', ('14', 2290)), ('4wq1.nx', ('14', 2291)), ('4wq1.nx', ('14', 2292)), 
# ('4v83.nx', ('BA', 2799)), ('4v83.nx', ('BA', 2800)), ('4v83.nx', ('BA', 2811)), ('4v83.nx', ('BA', 2812)), 
# ('4v83.nx', ('BA', 2813)), ('4wsm.nx', ('14', 2275)), ('4wsm.nx', ('14', 2276)), ('4wsm.nx', ('14', 2290)), 
# ...



#motif_dictionary for 3000th node so 5-motif in mac maga and meta
#{'instance1': ['4wf9.nx.X.2055', '4wf9.nx.X.2060', '4wf9.nx.X.603', '4wf9.nx.X.604', '4wf9.nx.X.605'], 'instance2': ['1vqn.nx.0.2068', '1vqn.nx.0.2073', '1vqn.nx.0.616', '1vqn.nx.0.617', '1vqn.nx.0.618'], 'instance3': ['4v6e.nx.DA.2028', '4v6e.nx.DA.560', '4v6e.nx.DA.561', '4v6e.nx.DA.562', '4v6e.nx.DA.2033'], 'instance4': ['5xxu.nx.2.1408', '5xxu.nx.2.1385', '5xxu.nx.2.1386', '5xxu.nx.2.1387', '5xxu.nx.2.1404'], 'instance5': ['4v5k.nx.DA.1992', '4v5k.nx.DA.1997', '4v5k.nx.DA.577', '4v5k.nx.DA.578', '4v5k.nx.DA.579'], 'instance6': ['4v8p.nx.H1.2365', '4v8p.nx.H1.2370', '4v8p.nx.H1.658', '4v8p.nx.H1.659', '4v8p.nx.H1.660'], 'instance7': ['5lzs.nx.9.1453', '5lzs.nx.9.1454', '5lzs.nx.9.1455', '5lzs.nx.9.1472', '5lzs.nx.9.1476'], 'instance8': ['4y4o.nx.2A.2054', '4y4o.nx.2A.583', '4y4o.nx.2A.584', '4y4o.nx.2A.582', '4y4o.nx.2A.2049'], 'instance9': ['4v8n.nx.BA.2055', '4v8n.nx.BA.2050', '4v8n.nx.BA.583', '4v8n.nx.BA.584', '4v8n.nx.BA.585'], 'instance10': ['5aj0.nx.A2.3846', '5aj0.nx.A2.3851', '5aj0.nx.A2.1294', '5aj0.nx.A2.1295', '5aj0.nx.A2.1296'], 'instance11': ['4wq1.nx.1H.584', '4wq1.nx.1H.2056', '4wq1.nx.1H.585', '4wq1.nx.1H.586', '4wq1.nx.1H.2051'], 'instance12': ['4v9q.nx.AA.2023', '4v9q.nx.AA.2028', '4v9q.nx.AA.579', '4v9q.nx.AA.580', '4v9q.nx.AA.581'], 'instance13': ['4wsm.nx.14.584', '4wsm.nx.14.2051', '4wsm.nx.14.2056', '4wsm.nx.14.585', '4wsm.nx.14.586'], 'instance14': ['3jbu.nx.b.2028', '3jbu.nx.b.560', '3jbu.nx.b.561', '3jbu.nx.b.562', '3jbu.nx.b.2033'], 'instance15': ['5xxb.nx.1.462', '5xxb.nx.1.463', '5xxb.nx.1.464', '5xxb.nx.1.465', '5xxb.nx.1.540'], 'instance16': ['4v9q.nx.CA.579', '4v9q.nx.CA.580', '4v9q.nx.CA.581', '4v9q.nx.CA.2023', '4v9q.nx.CA.2028'], 'instance17': ['4ioa.nx.X.569', '4ioa.nx.X.570', '4ioa.nx.X.571', '4ioa.nx.X.2011', '4ioa.nx.X.2016'], 'instance18': ['4v9i.nx.BA.2055', '4v9i.nx.BA.584', '4v9i.nx.BA.585', '4v9i.nx.BA.583', '4v9i.nx.BA.2050'], 'instance19': ['6gsl.nx.14.2056', '6gsl.nx.14.585', '6gsl.nx.14.586', '6gsl.nx.14.584', '6gsl.nx.14.2051'], 'instance20': ['4v5k.nx.BA.1992', '4v5k.nx.BA.1997', '4v5k.nx.BA.577', '4v5k.nx.BA.578', '4v5k.nx.BA.579'], 'instance21': ['5ibb.nx.14.2051', '5ibb.nx.14.2056', '5ibb.nx.14.584', '5ibb.nx.14.585', '5ibb.nx.14.586'], 'instance22': ['4v84.nx.DA.579', '4v84.nx.DA.580', '4v84.nx.DA.581', '4v84.nx.DA.2023', '4v84.nx.DA.2028'], 'instance23': ['1qvf.nx.0.616', '1qvf.nx.0.617', '1qvf.nx.0.618', '1qvf.nx.0.2068', '1qvf.nx.0.2073'], 'instance24': ['5gah.nx.A.2028', '5gah.nx.A.560', '5gah.nx.A.2033', '5gah.nx.A.562', '5gah.nx.A.561'], 'instance25': ['5l3p.nx.A.2033', '5l3p.nx.A.562', '5l3p.nx.A.561', '5l3p.nx.A.2028', '5l3p.nx.A.560'], 'instance26': ['4w29.nx.BA.2023', '4w29.nx.BA.2028', '4w29.nx.BA.579', '4w29.nx.BA.580', '4w29.nx.BA.581'], 'instance27': ['4v83.nx.BA.579', '4v83.nx.BA.580', '4v83.nx.BA.581', '4v83.nx.BA.2023', '4v83.nx.BA.2028'], 'instance28': ['4v7m.nx.BA.582', '4v7m.nx.BA.2054', '4v7m.nx.BA.583', '4v7m.nx.BA.584', '4v7m.nx.BA.2049'], 'instance29': ['5j7l.nx.DA.2033', '5j7l.nx.DA.2028', '5j7l.nx.DA.560', '5j7l.nx.DA.561', '5j7l.nx.DA.562'], 'instance30': ['4v85.nx.BA.2028', '4v85.nx.BA.560', '4v85.nx.BA.2033', '4v85.nx.BA.562', '4v85.nx.BA.561'], 'instance31': ['6eri.nx.AA.572', '6eri.nx.AA.570', '6eri.nx.AA.2042', '6eri.nx.AA.571', '6eri.nx.AA.2047'], 'instance32': ['4wsm.nx.1H.2051', '4wsm.nx.1H.584', '4wsm.nx.1H.585', '4wsm.nx.1H.586', '4wsm.nx.1H.2056'], 'instance33': ['4tue.nx.RA.2049', '4tue.nx.RA.582', '4tue.nx.RA.2054', '4tue.nx.RA.584', '4tue.nx.RA.583'], 'instance34': ['5lzs.nx.5.872', '5lzs.nx.5.873', '5lzs.nx.5.874', '5lzs.nx.5.2571', '5lzs.nx.5.2576'], 'instance35': ['4v9i.nx.DA.583', '4v9i.nx.DA.2055', '4v9i.nx.DA.584', '4v9i.nx.DA.585', '4v9i.nx.DA.2050'], 'instance36': ['5v7q.nx.A.662', '5v7q.nx.A.663', '5v7q.nx.A.664', '5v7q.nx.A.2266', '5v7q.nx.A.2271'], 'instance37': ['4v7m.nx.DA.582', '4v7m.nx.DA.2054', '4v7m.nx.DA.583', '4v7m.nx.DA.584', '4v7m.nx.DA.2049'], 'instance38': ['5ib8.nx.14.585', '5ib8.nx.14.2051', '5ib8.nx.14.584', '5ib8.nx.14.2056', '5ib8.nx.14.586'], 'instance39': ['4y4o.nx.1A.2049', '4y4o.nx.1A.583', '4y4o.nx.1A.582', '4y4o.nx.1A.2054', '4y4o.nx.1A.584'], 'instance40': ['3j79.nx.A.2663', '3j79.nx.A.712', '3j79.nx.A.713', '3j79.nx.A.714', '3j79.nx.A.2668'], 'instance41': ['6gsk.nx.14.585', '6gsk.nx.14.2051', '6gsk.nx.14.584', '6gsk.nx.14.2056', '6gsk.nx.14.586'], 'instance42': ['4v6e.nx.BA.2033', '4v6e.nx.BA.2028', '4v6e.nx.BA.560', '4v6e.nx.BA.561', '4v6e.nx.BA.562'], 'instance43': ['5tbw.nx.1.2178', '5tbw.nx.1.579', '5tbw.nx.1.580', '5tbw.nx.1.581', '5tbw.nx.1.2183'], 'instance44': ['5o2r.nx.A.2028', '5o2r.nx.A.560', '5o2r.nx.A.2033', '5o2r.nx.A.561', '5o2r.nx.A.562'], 'instance45': ['5j7l.nx.CA.2028', '5j7l.nx.CA.560', '5j7l.nx.CA.561', '5j7l.nx.CA.2033', '5j7l.nx.CA.562'], 'instance46': ['6cfj.nx.1A.2049', '6cfj.nx.1A.582', '6cfj.nx.1A.2054', '6cfj.nx.1A.583', '6cfj.nx.1A.584'], 'instance47': ['3cd6.nx.0.2074', '3cd6.nx.0.617', '3cd6.nx.0.618', '3cd6.nx.0.619', '3cd6.nx.0.2069'], 'instance48': ['5o60.nx.A.2257', '5o60.nx.A.2252', '5o60.nx.A.652', '5o60.nx.A.653', '5o60.nx.A.654'], 'instance49': ['4v6d.nx.BA.560', '4v6d.nx.BA.561', '4v6d.nx.BA.562', '4v6d.nx.BA.2033', '4v6d.nx.BA.2028'], 'instance50': ['4v9k.nx.DA.579', '4v9k.nx.DA.580', '4v9k.nx.DA.581', '4v9k.nx.DA.2023', '4v9k.nx.DA.2028'], 'instance51': ['4v8q.nx.AA.583', '4v8q.nx.AA.2055', '4v8q.nx.AA.584', '4v8q.nx.AA.585', '4v8q.nx.AA.2050'], 'instance52': ['5xym.nx.A.655', '5xym.nx.A.2255', '5xym.nx.A.656', '5xym.nx.A.657', '5xym.nx.A.2260'], 'instance53': ['4v88.nx.A6.1408', '4v88.nx.A6.1412', '4v88.nx.A6.1389', '4v88.nx.A6.1390', '4v88.nx.A6.1391'], 'instance54': ['5fdv.nx.2A.2049', '5fdv.nx.2A.582', '5fdv.nx.2A.583', '5fdv.nx.2A.2054', '5fdv.nx.2A.584'], 'instance55': ['5xxu.nx.2.1152', '5xxu.nx.2.1616', '5xxu.nx.2.1619', '5xxu.nx.2.1620', '5xxu.nx.2.1621'], 'instance56': ['4v88.nx.A1.2375', '4v88.nx.A1.634', '4v88.nx.A1.635', '4v88.nx.A1.636', '4v88.nx.A1.2370'], 'instance57': ['5gah.nx.A.2424', '5gah.nx.A.2393', '5gah.nx.A.2394', '5gah.nx.A.2395', '5gah.nx.A.2392'], 'instance58': ['5t7v.nx.B.2054', '5t7v.nx.B.2059', '5t7v.nx.B.603', '5t7v.nx.B.604', '5t7v.nx.B.605'], 'instance59': ['4v6d.nx.DA.2033', '4v6d.nx.DA.562', '4v6d.nx.DA.561', '4v6d.nx.DA.2028', '4v6d.nx.DA.560'], 'instance60': ['5el4.nx.14.586', '5el4.nx.14.2051', '5el4.nx.14.584', '5el4.nx.14.2056', '5el4.nx.14.585'], 'instance61': ['6gsl.nx.1H.2051', '6gsl.nx.1H.2056', '6gsl.nx.1H.585', '6gsl.nx.1H.586', '6gsl.nx.1H.584'], 'instance62': ['4wq1.nx.14.585', '4wq1.nx.14.2051', '4wq1.nx.14.584', '4wq1.nx.14.2056', '4wq1.nx.14.586'], 'instance63': ['3j6b.nx.A.1933', '3j6b.nx.A.1928', '3j6b.nx.A.459', '3j6b.nx.A.460', '3j6b.nx.A.461'], 'instance64': ['5tbw.nx.A.1408', '5tbw.nx.A.1412', '5tbw.nx.A.1389', '5tbw.nx.A.1390', '5tbw.nx.A.1391'], 'instance65': ['3jbv.nx.b.2028', '3jbv.nx.b.560', '3jbv.nx.b.2033', '3jbv.nx.b.562', '3jbv.nx.b.561'], 'instance66': ['4v8p.nx.D1.658', '4v8p.nx.D1.659', '4v8p.nx.D1.660', '4v8p.nx.D1.2365', '4v8p.nx.D1.2370'], 'instance67': ['4xej.nx.B23S.579', '4xej.nx.B23S.580', '4xej.nx.B23S.581', '4xej.nx.B23S.2023', '4xej.nx.B23S.2028'], 'instance68': ['4v8p.nx.F1.658', '4v8p.nx.F1.659', '4v8p.nx.F1.660', '4v8p.nx.F1.2365', '4v8p.nx.F1.2370'], 'instance69': ['4v88.nx.A5.2375', '4v88.nx.A5.634', '4v88.nx.A5.635', '4v88.nx.A5.636', '4v88.nx.A5.2370'], 'instance70': ['5ibb.nx.1H.2051', '5ibb.nx.1H.2056', '5ibb.nx.1H.584', '5ibb.nx.1H.585', '5ibb.nx.1H.586'], 'instance71': ['5e81.nx.1H.585', '5e81.nx.1H.2051', '5e81.nx.1H.584', '5e81.nx.1H.2056', '5e81.nx.1H.586'], 'instance72': ['5e81.nx.14.2051', '5e81.nx.14.2056', '5e81.nx.14.585', '5e81.nx.14.586', '5e81.nx.14.584'], 'instance73': ['4v88.nx.A2.1412', '4v88.nx.A2.1389', '4v88.nx.A2.1390', '4v88.nx.A2.1391', '4v88.nx.A2.1408'], 'instance74': ['3j9w.nx.BA.2057', '3j9w.nx.BA.2062', '3j9w.nx.BA.604', '3j9w.nx.BA.605', '3j9w.nx.BA.606'], 'instance75': ['6cfj.nx.2A.2054', '6cfj.nx.2A.2049', '6cfj.nx.2A.582', '6cfj.nx.2A.583', '6cfj.nx.2A.584'], 'instance76': ['4xej.nx.A23S.579', '4xej.nx.A23S.580', '4xej.nx.A23S.581', '4xej.nx.A23S.2023', '4xej.nx.A23S.2028'], 'instance77': ['4tue.nx.YA.582', '4tue.nx.YA.2049', '4tue.nx.YA.2054', '4tue.nx.YA.583', '4tue.nx.YA.584'], 'instance78': ['4v9f.nx.0.2062', '4v9f.nx.0.2067', '4v9f.nx.0.610', '4v9f.nx.0.611', '4v9f.nx.0.612'], 'instance79': ['5jup.nx.A.1391', '5jup.nx.A.1408', '5jup.nx.A.1412', '5jup.nx.A.1389', '5jup.nx.A.1390'], 'instance80': ['5ib8.nx.1H.2051', '5ib8.nx.1H.2056', '5ib8.nx.1H.584', '5ib8.nx.1H.586', '5ib8.nx.1H.585'], 'instance81': ['4v8n.nx.DA.2050', '4v8n.nx.DA.2055', '4v8n.nx.DA.583', '4v8n.nx.DA.584', '4v8n.nx.DA.585'], 'instance82': ['5mrc.nx.A.1928', '5mrc.nx.A.459', '5mrc.nx.A.460', '5mrc.nx.A.1933', '5mrc.nx.A.461'], 'instance83': ['6gsk.nx.1H.2051', '6gsk.nx.1H.584', '6gsk.nx.1H.585', '6gsk.nx.1H.586', '6gsk.nx.1H.2056'], 'instance84': ['4wt8.nx.C1.2043', '4wt8.nx.C1.2048', '4wt8.nx.C1.577', '4wt8.nx.C1.578', '4wt8.nx.C1.576'], 'instance85': ['4w29.nx.DA.2028', '4w29.nx.DA.579', '4w29.nx.DA.580', '4w29.nx.DA.581', '4w29.nx.DA.2023'], 'instance86': ['5ool.nx.A.171', '5ool.nx.A.172', '5ool.nx.A.173', '5ool.nx.A.1021', '5ool.nx.A.1026'], 'instance87': ['6d9j.nx.2.1309', '6d9j.nx.2.1313', '6d9j.nx.2.1290', '6d9j.nx.2.1291', '6d9j.nx.2.1292'], 'instance88': ['1vq6.nx.0.616', '1vq6.nx.0.617', '1vq6.nx.0.618', '1vq6.nx.0.2068', '1vq6.nx.0.2073'], 'instance89': ['5jup.nx.B.634', '5jup.nx.B.635', '5jup.nx.B.636', '5jup.nx.B.2370', '5jup.nx.B.2375'], 'instance90': ['5mmm.nx.A.2047', '5mmm.nx.A.570', '5mmm.nx.A.2042', '5mmm.nx.A.571', '5mmm.nx.A.572'], 'instance91': ['4v84.nx.BA.579', '4v84.nx.BA.580', '4v84.nx.BA.581', '4v84.nx.BA.2023', '4v84.nx.BA.2028'], 'instance92': ['4wt8.nx.D1.2043', '4wt8.nx.D1.2048', '4wt8.nx.D1.577', '4wt8.nx.D1.578', '4wt8.nx.D1.576'], 'instance93': ['4v8p.nx.A1.658', '4v8p.nx.A1.659', '4v8p.nx.A1.660', '4v8p.nx.A1.2365', '4v8p.nx.A1.2370'], 'instance94': ['5el4.nx.1H.2051', '5el4.nx.1H.584', '5el4.nx.1H.2056', '5el4.nx.1H.586', '5el4.nx.1H.585'], 'instance95': ['5tbw.nx.AR.2178', '5tbw.nx.AR.579', '5tbw.nx.AR.580', '5tbw.nx.AR.581', '5tbw.nx.AR.2183'], 'instance96': ['4v9k.nx.BA.579', '4v9k.nx.BA.580', '4v9k.nx.BA.581', '4v9k.nx.BA.2023', '4v9k.nx.BA.2028'], 'instance97': ['4v90.nx.BA.2050', '4v90.nx.BA.2055', '4v90.nx.BA.583', '4v90.nx.BA.584', '4v90.nx.BA.585'], 'instance98': ['5ju8.nx.BA.2033', '5ju8.nx.BA.2028', '5ju8.nx.BA.560', '5ju8.nx.BA.561', '5ju8.nx.BA.562'], 'instance99': ['5xy3.nx.1.409', '5xy3.nx.1.410', '5xy3.nx.1.411', '5xy3.nx.1.1888', '5xy3.nx.1.1893'], 'instance100': ['3j92.nx.5.905', '3j92.nx.5.906', '3j92.nx.5.907', '3j92.nx.5.2667', '3j92.nx.5.2672'], 'instance101': ['5lzd.nx.A.2028', '5lzd.nx.A.560', '5lzd.nx.A.561', '5lzd.nx.A.562', '5lzd.nx.A.2033'], 'instance102': ['5aj0.nx.B1.508', '5aj0.nx.B1.492', '5aj0.nx.B1.495', '5aj0.nx.B1.496', '5aj0.nx.B1.497'], 'instance103': ['6d9j.nx.5.2563', '6d9j.nx.5.869', '6d9j.nx.5.870', '6d9j.nx.5.871', '6d9j.nx.5.2568'], 'instance104': ['5tbw.nx.sR.1389', '5tbw.nx.sR.1390', '5tbw.nx.sR.1391', '5tbw.nx.sR.1408', '5tbw.nx.sR.1412'], 'instance105': ['4v4j.nx.w.2033', '4v4j.nx.w.584', '4v4j.nx.w.585', '4v4j.nx.w.586', '4v4j.nx.w.2028'], 'instance106': ['4v83.nx.DA.581', '4v83.nx.DA.2023', '4v83.nx.DA.2028', '4v83.nx.DA.579', '4v83.nx.DA.580'], 'instance107': ['5fdv.nx.1A.584', '5fdv.nx.1A.2049', '5fdv.nx.1A.582', '5fdv.nx.1A.2054', '5fdv.nx.1A.583'], 'instance108': ['5jte.nx.BA.2022', '5jte.nx.BA.2027', '5jte.nx.BA.560', '5jte.nx.BA.561', '5jte.nx.BA.562']}

def gkm(k):
		# where k is the layer of MAA
	mmd = {}
	n = 1
	for i in mmaga.nodes[list(mmaga.nodes())[k]]['node_set']:
		k = 'instance'+str(n)
		v = list(i)
		rrs=[]
		for j in v:
			r = list(mmg.reversed_node_map[j])
			rr = [r[0], list(r[1])]
			rrs.append(rr)
		mmd[k] = rrs
		n+=1
	return mmd




		
	# 	# saving the k-motif instances as a list of nodes in the maga graph
	# 	# then using the meta graph to reverse node_map these nodes to their pdbid-chain-residue identity
	# 	# store as dictionary instance: dot separated list
	# mmd = {}
	# for k,v in motif_dict.items():
	# 	rrs = []
	# 	for n in v:
	# 		r = list(mmg.reversed_node_map[n])
	# 		#rr = r[0]+'.'+list(r[1])[0]+'.'+str(list(r[1])[1])
	# 		rr = [r[0], list(r[1])]
	# 		rrs.append(rr)

	# 	mmd[k] = rrs
	# return mmd
	# # where k is the layer of MAA
	# motif_dict = {}
	# n = 1
	# for i in mmaga.nodes[list(mmaga.nodes())[k]]['node_set']:
	# 	motif_dict['instance'+str(n)] = list(i)
	# 	n+=1
	# 	# saving the k-motif instances as a list of nodes in the maga graph
	# 	# then using the meta graph to reverse node_map these nodes to their pdbid-chain-residue identity
	# 	# store as dictionary instance: dot separated list
	# mmd = {}
	# for k,v in motif_dict.items():
	# 	rrs = []
	# 	for n in v:
	# 		r = list(mmg.reversed_node_map[n])
	# 		#rr = r[0]+'.'+list(r[1])[0]+'.'+str(list(r[1])[1])
	# 		rr = [r[0], list(r[1])]
	# 		rrs.append(rr)

	# 	mmd[k] = rrs
	# return mmd

# for k in range(9404):
# 	try:
# 		nodes = mmaga.nodes[list(mmaga.nodes())[k]]['node_set']
# 	except KeyError:
# 		continue
# 	for i in nodes:
# 		print(k, '     ',str(len(list(i))))
# 		# all_dict[str(len(list(i)[0]))+'-motif'][str(k)+'-instance'] = get_instance_k_motif(k)
def smthn():
	print('loaded and now getting to work!')
	all_dict = {'1-motif':{},'2-motif':{},'3-motif':{},'4-motif':{},'5-motif':{},'6-motif':{},'7-motif':{}}
	 #of the form {'k_motif':{'n_type':{'instance#':[pdbid.nx.chain.residue]}}}
	for k in tqdm(range(9403)):
		if k in [952,953,954,955,956,957,959,960,961,962,964,965,966,967,969,972,977,984,994,999,1007,1081]:
			continue
		# try:
		# 	instances_same_k_type = mmaga.nodes[list(mmaga.nodes())[k]]['node_set']
		# 	#print('x')
		# except KeyError:
		# 	print(k)
		# 	continue

	# use for validating the motif with the website instanes

		# for k,v in get_instance_k_motif(k).items():
		# 	#print(v[0].split('.')[0])
		# 	if v[0].split('.')[0] in ['6th6','6rm3','5t2a','6zu5', '3j7q', '6uz7', '6s0x', '6agb', '5xyi', '6swa', '6gsl', '5lzs', '6swa', '5xxu', '6xyw', '6rxu', '5mrc', '6yxx', '3j7p', '5zwo', '1m5k', '6tz2', '6w2t']:
		# 		print(v)
	#

	# uncomment bellow for all_motifs

	#
		instances_same_k_type = mmaga.nodes[list(mmaga.nodes())[k]]['node_set']
		for i in instances_same_k_type:
		# 	print(i)
		# 	print(str(len(list(i)))+'-motif')
			all_dict[str(len(list(i)))+'-motif'][str(k)+'-type'] = get_instance_k_motif(k)
				#comes out empty for some reason run the above commented section

	#print(all_dict)

	pickle.dump(all_dict, open(os.path.join("results", "mggs", "dict_all_motifs.p"), 'wb'))
				
	pass















