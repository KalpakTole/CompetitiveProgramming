for _ in range(int(input())):
	N,K = map(int, input().split())
	S = list(map(int, input().split()))
	newlist = sorted(list(set(S)), reverse=True)
	val = newlist[K-1]
	newS = [ele for ele in S if ele>=val]
	print(len(newS))