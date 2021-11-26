for _ in range(int(input())):
	N = int(input())
	S = list(map(str, input().split()))
	cou = 0
	for i in range(N-1):
		for j in range(i+1,N):
			v1,v2 = S[i][0]+S[j][1:], S[j][0]+S[i][1:]
			if (v1 not in S) and (v2 not in S):
				print(v1,v2)
				cou += 2
	print(cou)