#import re
import os
def fixer(fpath, outid):
	pass
fpath = '/Users/owner1/Sync/vernal-project/cifs/instance_cifs'
outid='x'
files = os.listdir(fpath)
for f in files:
	if 'cif' in f:
		print(type(f))
		cfp = os.path.join(fpath,f)
		print(cfp)
		cf = open(cfp,'r')
		cfl = cf.readlines()
		cf.close()
		out = os.path.join(fpath, '/fixed','/fixed_'+outid+f)
		print(out)
		os.chdir('/Users/owner1/Sync/vernal-project/cifs/instance_cifs/fixed')
		fcf = open('fixed_'+f,'w')
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
#fixer('/Users/owner1/Sync/vernal-project/cifs/instance_cifs','x')