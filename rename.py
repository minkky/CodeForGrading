import os, glob

fpath = "*.py"

count = 1
for fpath in glob.glob(fpath):
	
	name = fpath.split('_')[0]
	name1 = fpath[-10:-3]
	filename = str(count) + '_' + name1 + '_' + name + '.py'
	print(filename)
	count = count + 1
	os.rename(fpath, filename)

