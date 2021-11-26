for _ in range(int(input())):
	S = int(input())
	Q = list(map(int, input().split()))
	total = 0
	for i in range(S):
		l = list(map(int, input().split()))
		total += sum(l[1:]) - ((l[0]-1) * Q[i])
	print(total)