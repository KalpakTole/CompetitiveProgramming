for _ in range(int(input())):
	N = int(input())
	B = list(map(int, input().split()))
	d = {i:B[i] for i in range(N)}
	d = {k:v for k,v in sorted(d.items(), key=lambda item:item[1])}
	counter = 0
	for k,v in d.items():
		if v > counter:
			d[k] = counter;
			counter += 1
	d = {k:v for k,v in sorted(d.items(), key=lambda item:item[0])}
	print(*d.values())