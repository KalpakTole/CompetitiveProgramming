def isPowerOfTwo (x): 
	return (x and (not(x & (x - 1))))

for _ in range(int(input())):
	N = int(input())
	if isPowerOfTwo(N):
		print(-1)
		continue
	else:
		L = [i for i in range(1,N+1)]
		li = [L.pop(0)]
		while L:
			val = L.pop(0)
			if li[-1] & val > 0:
				li.append(val)
			elif li[0] & val > 0:
				li.insert(0,val)
			else:
				L.insert(1,val)
		print(*li)