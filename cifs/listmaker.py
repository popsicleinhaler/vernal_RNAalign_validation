#import re
import os
def fixer(fpath, outid):
	pass
fpath = os.path.join(os.getcwd(),'instance_cifs', '3609_dir_2','fixed')
#os.mkdir(os.path.join(os.getcwd(),'instance_cifs', '3609_dir_2', 'fixed'))
out = os.path.join(fpath,'fixedlist_3609')
lister = open(out,'w')
files = os.listdir(fpath)
for f in files:
	if 'cif' in f:
		lister.write(f+'\n')
lister.close()
#fixer('/Users/owner1/Sync/vernal-project/cifs/instance_cifs','x')