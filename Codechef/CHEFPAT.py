for _ in range(int(input())):
	N = int(input())
	A = list(map(int, input().split()))
	d = {i:A[i] for i in range(N)}
	d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
	val = 1
	li = [0]*N
	for k in d.keys():
		li[k] = val
		val+=1
	print(*li)