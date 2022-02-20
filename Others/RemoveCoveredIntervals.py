# intervals = [[1,4],[3,6],[2,8]]
# intervals = [[3,10],[4,10],[5,11]]
# intervals = [[34335,39239],[15875,91969],[29673,66453],[53548,69161],[40618,93111]]
intervals = [[i,100000-i] for i in range(1000)]
# print(intervals)
n = len(intervals)
indices_to_remove = []
for i in range(n-1):
	num1 = intervals[i][0]
	num2 = intervals[i][1]
	for j in range(i+1,n):
		if num1 <= intervals[j][0] and num2 >= intervals[j][1]:
			indices_to_remove.append(j)
		elif num1 >= intervals[j][0] and num2 <= intervals[j][1]:
			indices_to_remove.append(i)
print(n-len(set(indices_to_remove)))