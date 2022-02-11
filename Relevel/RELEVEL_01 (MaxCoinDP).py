for _ in range(int(input())):

  N = int(input())
  ipMatrix = []
  for i in range(3):
    row = list(map(int, input().split()))
    ipMatrix.append(row)

  dp = [[0 for i in range(N)] for j in range(3)]

  dp[0][0] = ipMatrix[0][0]
  dp[1][0] = ipMatrix[1][0]
  dp[2][0] = ipMatrix[2][0]

  for j in range(1,N):
    dp[0][j] = max(dp[0][j-1] + ipMatrix[0][j], dp[0][j-1] + ipMatrix[1][j])

    dp[1][j] = max(dp[1][j-1] + ipMatrix[0][j], dp[1][j-1] + ipMatrix[1][j], dp[1][j-1] + ipMatrix[2][j])

    dp[2][j] = max(dp[2][j-1] + ipMatrix[1][j], dp[2][j-1] + ipMatrix[2][j])

  # print(dp)
  print(max(dp[0][N-1], dp[1][N-1], dp[2][N-1]))
