import numpy
N = int(input())
S = list(map(int, input().split()))
cur = 0
li = [cur]
for i in range(N):
	if S[i] == 1:
		cur += 1
	else:
		cur -= 1
	li.append(cur)
# print(li)

ans = []
for i in range(len(li)):
	if li[i] == 0:
		ans.append(i)
# print(ans)
d = {}
for i in range(len(ans)-1):
	d[ans[i]+1] = ans[i+1]-ans[i]
# print(d)
m = max(list(d.values()))
ki = [k for k,v in d.items() if v == m]

print(numpy.max(li), numpy.argmax(li), m, min(ki))