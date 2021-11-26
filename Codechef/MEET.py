def convert_time(h,m,f):
	if f=='PM':
		if h!=12:
			h+=12
	else:
		if h==12:
			h=0
	sol = str(h)+str(m)
	return int(sol)

for _ in range(int(input())):
	P = input().split()
	a = P[0].split(':')
	h = int(a[0])
	m = a[1]
	f = P[1]
	sol = convert_time(h,m,f)
	N = int(input())
	ans = ''
	for i in range(N):
		t = input().split()
		a1 = t[0].split(':')
		a2 = t[2].split(':')
		h1,m1,f1 = int(a1[0]), a1[1], t[1]
		h2,m2,f2 = int(a2[0]), a2[1], t[3]
		sol1 = convert_time(h1,m1,f1)
		sol2 = convert_time(h2,m2,f2)
		if sol1<=sol<=sol2:
			ans += '1'
		else:
			ans += '0'
	print(ans)
