# cook your dish here
for _ in range(int(input())):
	M,H = map(int, input().split())
	bmi = M//(H**2)
	if bmi <= 18:
		print(1)
	elif 19 <= bmi <= 24:
		print(2)
	elif 25 <= bmi <= 29:
		print(3)
	else:
		print(4)