for _ in range(int(input())):
	N,M = map(int, input().split())
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))
	A.sort()
	B.sort(reverse=True)
	c = 0
	if sum(A)>sum(B):
		print(c)
		continue
	flag = False
	for i in range(min(N,M)):
		A[i],B[i] = B[i],A[i]
		c+=1
		if sum(A)>sum(B):
			print(c)
			flag = True
			break
	if flag==False:
		print(-1)