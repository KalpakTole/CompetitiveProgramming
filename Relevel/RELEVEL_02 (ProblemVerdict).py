N,M = map(int, input().split())
d = {x: [0,False] for  x in range(1,N+1)}
for i in range(M):
	pno,verdict = input().split()
	if verdict != 'AC' and d[int(pno)][1] == False:
		d[int(pno)][0] += 1
	elif verdict == 'AC':
		d[int(pno)][1] = True
# print(d)
score, penalties = 0,0
for k,v in d.items():
	if v[1] == True:
		score += 100
		penalties += v[0]
print(score,penalties)
