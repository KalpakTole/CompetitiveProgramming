for _ in range(int(input())):
	s = input()
	n = len(s)
	x = s[:n//2]
	y = s[::-1][:n//2]
	if sorted(x) == sorted(y):
		print('YES')
	else:
		print('NO')