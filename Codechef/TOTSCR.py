for _ in range(int(input())):
	N,K = map(int, input().split())
	A = list(map(int, input().split()))
	for i in range(N):
		S = input()
		tot = 0
		for j in range(K):
			if S[j] == '1':
				tot += A[j]
		print(tot)
