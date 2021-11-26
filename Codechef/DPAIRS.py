N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
s = set()
co = 0
flag = True
for i in range(N):
	if flag:
		for j in range(M):
			val = A[i] + B[j]
			if val not in s:
				s.union({val})
				print(i,j)
				co += 1
				if co == (N+M-1):
					flag = False
					break
	else:
		break