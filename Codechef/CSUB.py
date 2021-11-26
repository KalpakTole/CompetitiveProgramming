for _ in range(int(input())):
	N = int(input())
	S = input()
	total = S.count('1')
	c = 1
	for i in range(1,N):
		if S[i] == '1':
			total += c
			c += 1
	print(total)