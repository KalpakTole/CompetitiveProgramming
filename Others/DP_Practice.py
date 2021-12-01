arr = list(map(int, input('Enter space separated positive integers:\n').split()))
dp = {0:arr[0], 1: max(arr[0],arr[1])}

for i in range(2,len(arr)):
	dp[i] = max(dp[i-1], dp[i-2]+arr[i])
print(dp)