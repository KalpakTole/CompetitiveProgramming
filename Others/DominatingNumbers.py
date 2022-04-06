def count_factors(x):
	co = 0
	for i in range(1,int(x**0.5)+1):
		if not x % i:
			if x / i == i:
				co += 1
			else:
				co += 2
	return co

for _ in range(int(input())):
	X,Y,K,N = list(map(int, input().split()))
	X,Y = min(X,Y), max(X,Y)
	M = 998244353
	start = X*N
	end = Y*N
	factors = []
	# 6 13 20 27
	for i in range(start, end+1, Y-X):
		ans = count_factors(i)
		factors.append(ans)
	indices = [i for i in range(len(factors)) if factors[i] > K]
	tot = 0
	for ele in indices:
		y = ele
		x = N - ele
		tot += ((x * y) + 1 ) % M
	print(tot%M)