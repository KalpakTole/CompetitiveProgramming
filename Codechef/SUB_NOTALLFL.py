for _ in range(int(input())):
	N,K = map(int, input().split())
	A = list(map(int, input().split()))
	if N == 1:
		print(1)
		continue
	s = [0]
	cur = A[0]
	for i in range(1,N):
		if A[i] != cur:
			cur = A[i]
			s.append(i)
	# print(s)
	if len(s) == 1:
		print(N)
		continue
	z = []
	for i in range(len(s)-1):
		z.append(s[i+1]-s[i])
	# print(z)
	print(max(z))