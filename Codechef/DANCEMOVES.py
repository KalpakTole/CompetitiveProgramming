for _ in range(int(input())):
	X, Y = map(int, input().split())
	if X > Y:
		print(X-Y)
		continue
	ans = Y - X
	if ans%2:
		final = ans//2 + 2
	else:
		final = ans//2
	print(final)