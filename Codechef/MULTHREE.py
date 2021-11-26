for _ in range(int(input())):
	K,d0,d1 = map(int, input().split())
	if K<10:
		tot = d0+d1
		for i in range(2,K):
			tot = tot + tot%10
		if tot%3==0:
			print('YES')
		else:
			print('NO')
	else:
		li = [d0,d1]
		tot = d0+d1
		for i in range(6):
			val = tot%10
			li.append(val)
			tot += val
		fili = li[4:8]
		if set(fili)=={0}:
			if sum(li)%3==0:
				print('YES')
			else:
				print('NO')
		else:
			inbetdig = ((K-4)//4)*2
			rema = K%4
			ans = sum(li[:4]) + inbetdig + sum(fili[:rema])
			if ans%3==0:
				print('YES')
			else:
				print('NO')