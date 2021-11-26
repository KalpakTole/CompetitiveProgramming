import numpy as np 
for _ in range(int(input())):
	N = int(input())
	S = list(map(int, input().split()))
	if S == sorted(S,reverse = True):
		print(sum(S))
		continue
	mvalue = np.min(S)
	tot = N * mvalue
	mindex = np.argmin(S)
	prevtot = mvalue
	while mindex!=0:
		mindex = np.argmin(S[:mindex])
		mvalue = S[mindex] - prevtot
		if mindex==0:
			tot += mvalue
		else:
			tot += (len(S[:mindex])+1) * mvalue
		prevtot += mvalue
	print(tot)