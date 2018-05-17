import os, glob

fpath = "*.py"

for fpath in glob.glob(fpath):
	
	name = fpath.split('_')[0]
	name1 = fpath[-10:-3]
	filename = name1 + '_' + name + '.py'
	print(filename)

	os.rename(fpath, filename)

