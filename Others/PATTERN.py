n = int(input())
if n>1:
	for i in range(n):
		val = ''
		for j in range(i):
			val += str(n-j)
		if i>0:
			print(*val,sep=' ',end=' ')
			print(*str(n-i)*(2*(n-i)-1),sep=' ',end=' ')
			print(*val[::-1])
		else:
			print(*str(n-i)*(2*(n-i)-1),sep=' ')

	for i in range(n-2,-1,-1):
		val = ''
		for j in range(i):
			val += str(n-j)
		if i>0:
			print(*val,sep=' ',end=' ')
			print(*str(n-i)*(2*(n-i)-1),sep=' ',end=' ')
			print(*val[::-1])
		else:
			print(*str(n-i)*(2*(n-i)-1),sep=' ')
else:
	print(1)