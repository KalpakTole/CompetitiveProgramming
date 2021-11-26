fh = open('a.txt','r')
line = fh.readline()
D,I,S,V,F = map(int, line.split())
streets = []
paths = []
for j in range(S):
	line = fh.readline()
	B,E,stname,L = map(str, line.split())
	B,E,L = int(B), int(E), int(L)
	streets += [B,E,stname,L]
for k in range(V):
	line = fh.readline()
	path = list(map(str, line.split()))
	paths += [int(path[0]), path[1:]]
