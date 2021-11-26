for _ in range(int(input())):
	S1 = [''] + list(input())
	S2 = [''] + list(input())
	X = input()
	li = []
	for i in range(len(S1)+1):
		for j in range(len(S2)+1):
			v1 = ''.join(S1[:i])
			v2 = ''.join(S2[:j])
			li.append(v1+v2)
	print(li)
	ans = [ele for ele in set(li) if ele in X]
	print(ans)
	print(len(ans))