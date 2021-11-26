for _ in range(int(input())):
	N,Z = map(int, input().split())
	A = list(map(int, input().split()))
	c = 0
	flag = False
	while set(A)!={0}:
		A.sort(reverse=True)
		val = A[0]
		A[0] = A[0]//2
		Z -= val
		c += 1
		if Z<1:
			print(c)
			flag = True
			break
	if flag == False:
		print('Evacuate')