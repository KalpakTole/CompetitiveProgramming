for _ in range(int(input())):
	S = input()
	best = 0
	co = 0
	for i in range(len(S)):
		if S[i]=='<':
			co += 1
		elif S[i]=='>':
			co -= 1
		if co == 0:
			best = i+1
		if co < 0:
			break
	print(best)