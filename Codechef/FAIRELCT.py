for _ in range(int(input())):
	N,M = map(int, input().split())
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))
	c = 0
	if sum(A)>sum(B):
		print(0)
		continue
	while sum(A)<=sum(B):
		miA,miB = A.index(min(A)), B.index(max(B))
		curAval = sum(A)
		A[miA],B[miB] = B[miB],A[miA]
		c+=1
		print(A)
		print(B)
		if sum(A)>sum(B):
			print(c)
			break
		if sum(A)<=curAval:
			print(-1)
			break