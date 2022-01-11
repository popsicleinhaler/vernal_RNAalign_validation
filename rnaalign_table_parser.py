import pickle
import numpy as np
import pandas as pd
import seaborn as sns
import numpy.random as rand
from statistics import mean
import os
import matplotlib.pyplot as plt

i = str(3662)

def builder(i):
	inters = os.path.join(os.getcwd(), 'cifs','instance_cifs','3680to3779-','Results',i+'_selfninter')
	selfie = os.path.join(os.getcwd(), 'cifs','instance_cifs','3680to3779-','Results',i+'_selfninter', 'self.txt')

	df = {'structure_name':[],'simvals':[], 'inter_or_intra':[]}

	strucs = os.listdir(inters)
	for s in strucs:
		spath = os.path.join(inters,s)
		inter_data = pd.read_csv(spath, delim_whitespace=True)
		inter_data = inter_data.iloc[:-1]
		struc1 = inter_data['#PDBchain1'].tolist()
		struc1_ids = []
		for i in struc1: #remove total at the end
			iD = i.split('/')[-1].split('.')[0]
			struc1_ids.append(iD)
		# fserch = struc1_ids[0]
		section_length = len(struc1_ids)
		df['structure_name'].extend(struc1_ids)
		df['simvals'].extend(inter_data['TM1'].tolist()[:section_length])
		df['inter_or_intra'].extend(['intra']*section_length)

	self_data = pd.read_csv(selfie, delim_whitespace=True)
	self_data=self_data.iloc[:-1]
	struc2 = self_data['#PDBchain1'].tolist()
	struc3 = self_data['PDBchain2'].tolist()
	struc2_ids = []
	struc3_ids = []
	for i in struc2: #remove total at the end
		iD = i.split('/')[-1].split('.')[0]
		struc2_ids.append(iD)
	for i in struc3: #remove total at the end
		iD = i.split('/')[-1].split('.')[0]
		struc3_ids.append(iD)
	section2_length = len(struc2_ids)
	df['structure_name'].extend(struc2_ids)
	df['structure_name'].extend(struc3_ids)
	df['simvals'].extend(self_data['TM1'].tolist()[:section2_length])
	df['simvals'].extend(self_data['TM1'].tolist()[:section2_length])
	df['inter_or_intra'].extend(['inter']*section2_length)
	df['inter_or_intra'].extend(['inter']*section2_length)
	return df

for i in range(3682,3695):
	i=str(i)
	df = builder(i)
	dframe = pd.DataFrame(df)
	dframe.explode('simvals')
	dframe['simvals']=dframe['simvals'].astype('float')
	dframe.to_csv('test_dataframe_prepforplot.txt',index=False, sep=' ')

	plt.figure(figsize=(250,50))
	plt.axhline(y=.45, linewidth=2, color = 'red', label='threshold of similarity (higher the better)')
	ax = sns.boxplot(x="structure_name", y="simvals", hue="inter_or_intra",data=dframe, palette="Set3")
	figure = ax.get_figure()    
	figure.savefig(os.path.join(os.getcwd(), i+'_RNAalign_3680to3779_.png'))

