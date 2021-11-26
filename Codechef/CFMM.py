for _ in range(int(input())):
	N = int(input())
	d = {x:0 for x in 'codehf'}
	for i in range(N):
		S = input()
		for ele in S:
			if ele in d.keys():
				d[ele] += 1
	d['c'] = d['c']//2
	d['e'] = d['e']//2
	print(min(d.values()))