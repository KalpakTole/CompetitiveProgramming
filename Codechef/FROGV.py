N,K,P = map(int, input().split())
A = list(map(int, input().split()))
d = {A[i]:i+1 for i in range(N)}
all_segments = []
A.sort()
sp,ep = 0,0
cp,np = 0,0
while np+1<N:
	if abs(A[cp]-A[np+1]) <= K:
		cp = cp+1
		np = np+1
		ep = np
	elif sp != ep:
		all_segments.append([d[A[sp]],A.index(A[ep])-A.index(A[sp])+1])
		cp,np = np+1,np+1
		sp = cp
		ep = np
print(all_segments)

for i in range(P):
	A,B = map(int, input().split())
	flag = False
	for ele in all_segments:
		if A>=ele[0] and B<=ele[1]:
			print("Yes")
			flag = True
			break
	if flag == False:
		print('No')
	