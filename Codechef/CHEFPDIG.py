d = {str(x):chr(x) for x in range(65,91)}
for _ in range(int(input())):
	N = input()
	S = set(N)
	fin = ''
	for k,v in d.items():
		if set(k).issubset(S):
			if len(set(k))==1:
				if N.count(k[0])>1:
					fin += v
			else:
				fin += v
	print(fin)