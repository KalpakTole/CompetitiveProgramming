def majorityElement(A, N):
	#Your code here
	d = {}
	for i in A:
		d[str(i)] = d.get(str(i), 0) + 1
	print(d)
	d = {k: v for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True)}
	print(d)
	if list(d.values())[0] > N//2:
		return list(d.keys())[0]
	else:
		return -1


with open(r'C:\Users\kalpa\Downloads\fileInput.txt','r') as f:
	l = list(f)
	N = int(l[0])
	A = list(map(int, l[1].split()))

ans = majorityElement(A,N)
print(ans)