for _ in range(int(input())):
	N,D = map(str, input().split())
	if D not in N:
		print(0)
	else:
		tot = 0
		while D in N:
			ind = N[::-1].index(D)
			if ind==0:
				val = 10**ind
			else:
				val = 10**ind - int(N[-ind:])
			N = str(int(N)+val)
			tot += val
		print(tot)