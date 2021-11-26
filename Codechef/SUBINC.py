for _ in range(int(input())):
	N = int(input())
	A = list(map(int, input().split()))
	li = []
	c = 0
	val = A[0]
	for i in range(N):
		if A[i]>=val:
			c+=1
			val = A[i]
		else:
			li.append(c)
			c = 1
			try:
				val = A[i]
			except:
				break
	if c!=0:
		li.append(c)
	# print(li)
	ans = [N]
	for ele in li:
		co = (ele*(ele-1))//2
		ans.append(co)
	print(sum(ans))