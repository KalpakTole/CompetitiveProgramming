def solution(n,m,obstacles,teleports):
	target = (n-1,m-1)
	obstacles = [(ele[0],ele[1]) for ele in obstacles]
	current = (0,0)
	visited = set([(0,0)])
	teles = {}
	for ele in teleports:
		teles[(ele[0],ele[1])] = (ele[2],ele[3])
	count = 1
	while current!=target:
		if current in obstacles:
			return -1
		elif current in teles:
			current = teles[current]
			if current in visited:
				return -2
			visited = visited.union([current])
			count += 1
		if current[1]+1>target[1]:
			return -1
		elif current==target:
			return count
		else:
			current = (current[0],current[1]+1)
			count += 1
			visited = visited.union([current])
	return count
	

def main():
	n = 3
	m = 4
	obstacles = [[2,0],[1,0]]
	teleports = [[0,1,1,1],[1,2,0,2],[0,3,2,1]]
	ans = solution(n,m,obstacles,teleports)
	print(ans)

main()