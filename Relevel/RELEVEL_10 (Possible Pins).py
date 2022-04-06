for _ in range(int(input())):
	D1,D2 = list(map(int, input().split()))
	if D1==0 and D2==0:
		ans = (10-D1)*(10-D2)
	elif D1==0:
		ans = (10-D1)*2*(10-D2)
	elif D2==0:
		ans = 2*(10-D1)*(10-D2)
	else:
		ans = 2*(10-D1) * 2*(10-D2)
	print(ans)