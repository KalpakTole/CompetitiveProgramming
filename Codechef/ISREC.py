for _ in range(int(input())):
	N,M = map(int, input().split())
	grid = []
	for i in range(N):
		line = list(input())
		grid.append(line)
	
	tr,lr = False, False
	top, bottom, left, right = 0,0,0,0
	for i in range(N):
		for j in range(M):
			if grid[i][j] == '1':
				if tr == False:
					top = i
					tr = True
				if lr == False:
					left = j
					lr = True
				if i>bottom:
					bottom = i
				if j>right:
					right = j

	flag = True
	for i in range(N):
		if flag:
			for j in range(M):
				if top <= i <= bottom and left <= j <= right:
					if grid[i][j] == '0':
						print('NO')
						flag = False
						break
		if flag == False:
			break
	if flag:
		print('YES')