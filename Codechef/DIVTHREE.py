for _ in range(int(input())):
	N,K,D = list(map(int, input().split()))
	A = list(map(int, input().split()))
	val = sum(A)//K
	if val>D:
		print(D)
	else:
		print(val)