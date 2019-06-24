import sys, glob, os, time

fpath = '*'
dir = glob.glob(fpath)
dir = sorted(dir)

for path in dir:
	if os.path.isdir(path) and path != '0done':
		files = os.listdir(path)
		print("[", path, "]")
		for file in files:
			if '.py' in file:
				if input("all or not :0") == '0':
					continue

				if input("1 or not : 1") == '1':
					print('1st test\n')
					cmd  = 'python ' + os.path.join(path, file) + ' ./test1.csv 0.015 0.249'
					start = time.time()
					os.system(cmd)
					print('end : ', time.time() - start)

				if input("2 or not : 2") == '2':				
					print('\n2nd test\n')
					cmd  = 'python ' + os.path.join(path, file) + ' ./test2.csv 0.014 0.195'
					start = time.time()
					os.system(cmd)
					print('end : ', time.time() - start)

				if input("3 or not : 3") == '3':	
					print('\n3rd test\n')
					cmd  = 'python ' + os.path.join(path, file) + ' ./test3.csv 0.0119 0.2'
					start = time.time()
					os.system(cmd)
					print('end : ', time.time() - start)
				
	