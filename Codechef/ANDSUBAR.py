import math
for _ in range(int(input())):
	N = int(input())
	if N==1 or N==2:
		print(1)
		continue
	lp = 2**(math.floor(math.log(N,2)))
	slp = lp//2
	a1 = N-lp+1
	a2 = lp-slp
	print(max(a1,a2))