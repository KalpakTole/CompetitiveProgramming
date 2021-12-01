n = int(input())
cv = list(map(int, input().split()))
rhs = int(input())

dp = [0 for i in range(rhs + 1)]
dp[0] = 1
for i in range(n):
	for j in range(cv[i], rhs + 1):
		dp[j] += dp[j - cv[i]]

print(dp[rhs])