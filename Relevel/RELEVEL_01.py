import numpy as np
for _ in range(int(input())):
	N = int(input())
	mat = []
	for i in range(N):
		row = list(map(int, input().split()))
		mat.append(row)
	
	dp = [[0 for i in range(N)] for j in range(3)]
	dp[0][0] = mat[0][0]
	dp[1][0] = mat[1][0]
	dp[2][0] = mat[2][0]
	print(f'\n\n{dp=}')
	for j in range(1,N):
		arr = [dp[i][j-1] for i in range(3)]
		dp[0][j] = arr[0] + mat[i][j]
		dp[1][j] = arr[1] + mat[i][j]
		dp[2][j] = arr[2] + mat[i][j]
	print(f'\n\n{dp=}')