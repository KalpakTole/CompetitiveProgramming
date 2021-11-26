for _ in range(int(input())):
	D,C = map(int, input().split())
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))
	total1, total2 = 0,0
	# without coupon
	total1 = 2*D
	# with coupon
	if sum(A) < 150:
		total2 += D
	if sum(B) < 150:
		total2 += D
	total2 += C
	if total2 < total1:
		print('YES')
	else:
		print('NO')