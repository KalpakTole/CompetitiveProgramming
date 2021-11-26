for _ in range(int(input())):
	N = int(input())
	W = list(map(int, input().split()))
	L = list(map(int, input().split()))
	d = {W[i]:[i,L[i]] for i in range(N)}
	ind,nos = [],[]
	for k,v in sorted(d.items()):
		ind.append(v[0])
		nos.append(v[1])
	tot_hits = 0
	for i in range(1,N):
		while ind[i]<=ind[i-1]:
			ind[i] += nos[i]
			tot_hits += 1
	print(tot_hits)