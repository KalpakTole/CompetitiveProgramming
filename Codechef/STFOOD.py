for _ in range(int(input())):
	N = int(input())
	li = []
	for i in range(N):
		S,P,V = map(int, input().split())
		val = (P//(S+1))*V
		li.append(val)
	print(max(li))