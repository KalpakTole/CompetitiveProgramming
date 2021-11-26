from datetime import datetime, time
def convert_time(h,f):
	if f=='PM':
		if h!=12:
			h+=12
	else:
		if h==12:
			h=0
	return h

def is_time_between(begin_time, end_time, check_time):
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else:
        return check_time >= begin_time or check_time <= end_time

for _ in range(int(input())):
	P = input().split()
	a = P[0].split(':')
	h = int(a[0])
	m = int(a[1])
	f = P[1]
	N = int(input())
	ans = ''
	for i in range(N):
		t = input().split()
		a1 = t[0].split(':')
		a2 = t[2].split(':')
		h1,m1,f1 = int(a1[0]), int(a1[1]), t[1]
		h2,m2,f2 = int(a2[0]), int(a2[1]), t[3]
		if h1==h==h2 and m1==m==m2:
			if f1!=f:
				ans += '0'
				continue
		h = convert_time(h,f)
		h1 = convert_time(h1,f1)
		h2 = convert_time(h2,f2)
		if is_time_between(time(h1,m1), time(h2,m2), time(h,m)) == True:
			ans += '1'
		else:
			ans += '0'
	print(ans)