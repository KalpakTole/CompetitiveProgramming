for _ in range(int(input())):
	N = int(input())
	A = list(map(int, input().split()))
	perfect_squares = ''
	total = 0
	for num in A:
		if int(num**0.5) == num**0.5:
			perfect_squares += '1'
			total += 1
		else:
			perfect_squares += '0'
	seq = perfect_squares.split('0')
	for ele in seq:
		if ele:
			n = len(ele)
			total += (n*(n+1))//2 - n
	print(total)