N = 100
li = []
for i in range(N):
	if i^(i+1) == (i+2)^(i+3):
		li.append(i)
print(li)