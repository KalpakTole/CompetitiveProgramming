for _ in range(int(input())):
	N,K = map(int, input().split())
	A = list(map(int, input().split()))
	liK = set([i for i in range(1,K+1)])
	flag = False
	for i in range(N,0,-1):
		for j in range(0,N-i+1):
			newli = A[j:i+j]
			if liK - set(newli):
				print(len(newli))
				flag = True
				break
		if flag:
			break