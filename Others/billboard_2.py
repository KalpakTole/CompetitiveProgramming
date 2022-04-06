# M = 20
# x[]       = {6, 7, 12, 13, 14}
# revenue[] = {5, 6, 5,  3,  1}
# t = 3

M = 20
t = 5
x =   [6,   11,  12, 13,    14, 15]
rev = [100, 3,   1,  2000,  2,  2 ]

x = [6, 7, 12, 13, 14]
rev = [5, 6, 5,  3,  1]

# dp = [ 100, 103, 2100, 2100, 2100 ]
dp = [0]*len(x)
dp[0] = rev[0]
# lav = rev[0]
for i in range(1,len(x)):
	if x[i] - x[i-1] > t:
		dp[i] = max(dp[i-1] - rev[i-1] + rev[i], dp[i-1])
		# lav = dp[i] - dp[i-1]
	else:
		dp[i] = max(dp[i-1] - (dp[i-1] - dp[i-2]) + rev[i], dp[i-1])

print(dp)