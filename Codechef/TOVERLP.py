for _ in range(int(input())):
	N,M = map(int, input().split())
	s1,s2 = [],[]
	tot = 0
	for i in range(N):
		l = list(map(int, input().split()))
		s1.append(l)
	for i in range(M):
		l = list(map(int, input().split()))
		s2.append(l)
	for i in range(N):
		for j in range(M):
			strip1, strip2 = sorted([s1[i],s2[j]])
			if strip2[0] < strip1[1] and strip2[1] > strip1[0]:
				x1,x2,y1,y2 = strip1[0],strip1[1],strip2[0],strip2[1]
				if y1>=x1 and y2<=x2:
					tot += abs(y2-y1)
				else:
					tot += abs(y1-x2)
	print(tot)