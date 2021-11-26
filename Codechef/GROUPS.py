for _ in range(int(input())):
	S = input()
	tot = False
	c = 0
	for i in range(len(S)):
		if S[i] == '1' and tot == False:
			tot = True
			c += 1
		elif S[i] == '0' and tot == True:
			tot = False
	print(c)