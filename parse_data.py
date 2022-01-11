import pickle
import numpy as np
import pandas as pd
import seaborn as sns
import numpy.random as rand
from statistics import mean
import os
import matplotlib.pyplot as plt

def init():
	pass

i = 7991
i2 = 8001
filepath = os.path.join(os.getcwd(), 'data3_inter_'+str(i)+'n'+str(i2)+'.pkl')
print(filepath)
#'/Users/owner1/Sync/vernal-project/data_self_'+str(i)+'n'+str(i2)+'.pkl'
file = open(filepath, 'rb')
arr = pickle.load(file)
arr1 = arr['bt_smthn'][0]
#arr1 = arr['cluster'+str(i)][1]

df = pd.DataFrame(arr1)
xpath = os.path.join(os.getcwd(), 'check3_inter_'+str(i)+'n'+str(i2)+'.xlsx')
# print(xpath)
# #'/Users/owner1/Sync/vernal-project/check_inter_'+str(i)+'n'+str(i2)+'.xlsx'
df.to_excel(xpath, index=False)


def self_meanies(arr1):
	perstructure = {}
	instances = np.shape(arr1)[0] #int(len(gkm(i))/3)
	il = range(1, instances+1)
	for i in il:
		try:
			rownums = arr1[:,i][np.nonzero(arr1[:,i])]
			colnums = arr1[i,:][np.nonzero(arr1[i,:])]
			allnums = np.append(rownums,colnums)
		except IndexError:
			continue
		perstrmean = np.mean(allnums)
		perstructure[i]=perstrmean
	return perstructure

def self_perstr_sim(arr1):
	perstructure = {}
	instances = np.shape(arr1)[0] #int(len(gkm(i))/3)
	il = range(1, instances+1)
	for i in il:
		try:
			rownums = arr1[:,i][np.nonzero(arr1[:,i])]
			colnums = arr1[i,:][np.nonzero(arr1[i,:])]
			allnums = np.append(rownums,colnums)
		except IndexError:
			continue
		perstructure[i]=allnums
	return perstructure

def pers_QCP_sz(selfm,ref):
	filepath = os.path.join(os.getcwd(), 'data_self_8001n8028.pkl')
	file = open(filepath, 'rb')
	arr = pickle.load(file)
	arr1 = arr['cluster8001'][1]
	arrx = pd.read_excel(os.path.join(os.getcwd(), 'comaprison_8001to8103n8003.xlsx'))
	arrx = np.transpose(arrx.to_numpy())
	print(np.shape(arr1))
	print(np.shape(arrx))
	# print(arrx)
	print(arrx[1,3])
	print(arrx[1,1])
	perstructure = {} #{'name(i)':{'self':[],'ref':[]}}
	instances = min([np.shape(arrx)[0],np.shape(arr1)[0]]) #int(len(gkm(i))/3)
	il = range(1, instances+1)
	for i in il:
		try:
	 		rownums = arr1[:,i][np.nonzero(arr1[:,i])]
		 	colnums = arr1[i,:][np.nonzero(arr1[i,:])]
		 	allnums = np.append(rownums,colnums)
		 	colns = arrx[i,:][np.nonzero(arrx[i,:])]
		except IndexError:
			continue
		perstructure[i]={'self':allnums,'ref':colns}
	df = {'motif instance':[],'similarity':[], 'Legend':[]}
	for k,v in perstructure.items():
		ldata = len(v['self'])
		rdata = len(v['ref'])
		names = [k] * (ldata)
		names.extend([k]*rdata)
		hue = ['intracluster'] * ldata
		hue2 = ['intercluster'] * rdata
		df['motif instance'].extend(names)
		df['similarity'].extend(v['self'])
		df['similarity'].extend(v['ref'])
		df['Legend'].extend(hue)
		df['Legend'].extend(hue2)

	passdf = pd.DataFrame(df)
	ax = sns.boxplot(x="motif instance", y="similarity", hue="Legend",
	                 data=passdf, palette="Set3")
	figure = ax.get_figure()    
	figure.savefig(os.path.join(os.getcwd(), 'differnces_wref.png'), dpi=400)
		#return perstructure

	# 							# print(self_meanies(arr1))
	# 							# # print(self_meanies(arr2))
	# 							# i=8001
	# 							# i2=8003
	# 							# filepathx = os.path.join(os.getcwd(), 'data2_inter_'+str(i)+'n'+str(i2)+'.pkl')
	# 							# #'/Users/owner1/Sync/vernal-project/data_inter_'+str(i)+'n'+str(i2)+'.pkl'
	# 							# filex = open(filepathx, 'rb')
	# 							# arrx = pickle.load(filex)
	# 							# arrx = arrx['bt_smthn'][0]
	# 							# print(np.shape(arrx))
	# 							# df = pd.DataFrame(arrx)
	# 							# xpath = os.path.join(os.getcwd(), 'check2_inter_'+str(i)+'n'+str(i2)+'.xlsx')
	# 							# #'/Users/owner1/Sync/vernal-project/check_inter_'+str(i)+'n'+str(i2)+'.xlsx'
	# 							# df.to_excel(xpath, index=False)


def inter_meanies(arrx):
	pass

#need to build calss
#also this structure is retarded and should just put each structure as one dictionary elemnt
def build_df(perstructure,mean=True):
	df = {'structure_name':[],'simvals':[], 'inter_or_intra':[]}
	instances = np.shape(arr1)[0] #int(len(gkm(i))/3)
	il = range(1, instances+1)
	for i,v in perstructure.items():
		if mean:
			names = [str(i)]*2 
			hue = 'intra'
			hue2 = 'inter'
			df['structure_name'].extend(names)
			mean = sum(v)/len(v)
			df['simvals'].append(mean)
			 
			df['simvals'].append(sum(random_inter)/len(random_inter))
			df['inter_or_intra'].append(hue)
			df['inter_or_intra'].append(hue2)
		else:
			names = [str(i)] * (2*len(v))
			hue = ['intra'] * len(v)
			hue2 = ['inter'] * len(v)
			df['structure_name'].extend(names)
			df['simvals'].extend(v)
			random_parameter = rand.uniform(7.5,8,1)
			random_inter = rand.rayleigh(random_parameter,len(v))
			df['simvals'].extend(random_inter)
			df['inter_or_intra'].extend(hue)
			df['inter_or_intra'].extend(hue2)
	return df

def plot_boxes():
	df = pd.DataFrame(build_df(self_perstr_sim(arr1),mean=False))
	ax = sns.boxplot(x="structure_name", y="simvals", hue="inter_or_intra",
	                 data=df, palette="Set3")
	figure = ax.get_figure()    
	figure.savefig(os.path.join(os.getcwd(), 'data_7991vsf.png'), dpi=400)

def plot_scatter():

	#fen = build_df(self_perstr_sim(arr1))

# print(fen)
# for k,v in fen:
# 	print(k, len(v))
	df = pd.DataFrame(build_df(self_perstr_sim(arr1)))
	print(df)
	ax = sns.scatterplot(x="structure_name", y="simvals", hue="inter_or_intra",
	                 data=df, palette="Set3")
	figure = ax.get_figure()    
	figure.savefig(os.path.join(os.getcwd(), 'data_7991vsf.png'), dpi=400)


# need dataframe like index cluster1_perstructuresim structure_name_repeated inter_or_intra(as hue) 
# dict = {'structure_name'=[names corresponding to the ],'simvals'=[values of similarity matched to the names in the structure_name]}






#plot_boxes()