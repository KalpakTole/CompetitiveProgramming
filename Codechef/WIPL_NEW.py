import bisect
for _ in range(int(input())):
	N,K = map(int, input().split())
	H = list(map(int, input().split()))
	H.sort()
	mi,tr,c = 0,0,0
	curval = K
	while mi<K:
		try:
			mi += H.pop(bisect.bisect_left(H,curval))
			curval = K-mi
			c += 1
		except IndexError:
			if H:
				mi += H.pop(len(H)-1)
				c += 1
			else:
				c = -1
				break
	if c==-1:
		print(c)
		continue
	curval = K
	while tr<K:
		try:
			tr += H.pop(bisect.bisect_left(H,curval))
			curval = K-tr
			c += 1
		except IndexError:
			if H:
				tr += H.pop(len(H)-1)
				c += 1
			else:
				c = -1
				break
	print(c)