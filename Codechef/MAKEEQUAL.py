for _ in range(int(input())):
	N = int(input())
	A = list(map(int, input().split()))
	S = sorted(set(A))
	diff = 0
	for i in range(1,len(S)):
		diff += S[i] - S[i-1]
	print(diff)
	