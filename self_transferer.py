#add self comparison results to the results folder

#goal prepare comparison cluster
import os
from shutil import copy

whichset = '3680to3779-'

for i in range(3682,3708):
	fromthis = os.path.join(os.getcwd(), 'cifs','instance_cifs', str(i)+'_dir_','self.txt')
	tothis = os.path.join(os.getcwd(), 'cifs','instance_cifs', whichset, 'Results', str(i)+'_selfninter')
	copy(fromthis,tothis)