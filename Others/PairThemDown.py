for _ in range(int(input())):
	N = int(input())
	A = list(map(int, input().split()))
	A.sort()
	s = 0
	for i in range(N//2):
		s += (A[i]+A[N-1-i])**2
	print(s)