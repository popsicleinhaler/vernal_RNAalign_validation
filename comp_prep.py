#goal prepare comparison cluster
import os
from shutil import copy

def getitsid(clusterpath):
	return clusterpath.split("/")[-1].split('_')[0]

def compfolder(clusters):
	# ["C:\Users\boop\Sync\vernal-project\cifs\instance_cifs\3678_dir_"]
	pathtoend = os.path.join(os.getcwd(), 'cifs','instance_cifs', getitsid(clusters[0])+'to'+getitsid(clusters[-1])+'-')
	os.mkdir(pathtoend)
	for clust in clusters:
		iD = getitsid(clust)
		# merge all cifs into one folder and have len(custer) text files 
		# containing the names of all files except for those from 1 cluster
		src_files = os.listdir(clust)
		for struc in src_files:
			if 'cif' in struc:
				strucpath = os.path.join(clust,struc)
				copy(strucpath,pathtoend)
			else:
				listpath = os.path.join(pathtoend,'inter_list_'+iD)
				newlist = open(listpath,'a+')
				for c in clusters:
					if c != clust:
						pathtolist = os.path.join(clust,'ins_list_'+getitsid(clust))
						partlist = open(pathtolist,'r')
						newlist.write(partlist.read())

dataset = []
for i in range(3780,3801):
	out = os.path.join(os.getcwd(),'cifs','instance_cifs',str(i)+'_dir_')
	dataset.append(out)

compfolder(dataset)