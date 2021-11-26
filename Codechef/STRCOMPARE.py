for _ in range(int(input())):
	N = int(input())
	A = input()
	B = input()
	co = 0
	if A[N-1]<B[N-1]:
		for i in range(N):
			if A[i] <= B[i]:
				co += 1
	else:
		for i in range(N):
			if A[i] < B[i]:
				co += 1
	print(co)