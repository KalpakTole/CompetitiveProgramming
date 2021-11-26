import copy 
for _ in range(int(input())):
	N,K = map(int, input().split())
	H = list(map(int, input().split()))
	H.sort()
	J = copy.copy(H)
	mi,tr = 0,0
	c = 0
	flag = True
	while flag:
		if mi<K:
			try:
				mi += H.pop()
				c += 1
			except IndexError:
				ans = -1
				break
		if tr<K:
			try:
				tr += H.pop()
				c += 1
			except IndexError:
				ans = -1
				break
		if mi>=K and tr>=K:
			ans = c
			flag = False
		
	mi,tr,c=0,0,0
	while mi<K:
		try:
			mi += J.pop()
			c+=1
		except IndexError:
			ans2 = -1
			break
	while tr<K:
		try:
			tr += J.pop()
			c+=1
		except IndexError:
			ans2 = -1
			break
	if mi>=K and tr>=K:
		ans2 = c
	if ans==-1:
		print(ans2)
	elif ans2==-1:
		print(ans)
	else:
		print(min(ans,ans2))