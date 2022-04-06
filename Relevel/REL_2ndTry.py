for _ in range(int(input())):
	N = int(input())
	A = list(map(int, input().split()))
	M = 998244353
	d = {}
	found = ''
	for ele in A:
		d[ele] = d.get(ele,0) + 1
	for ele in A:
		if int(ele**0.5) == ele**0.5:
			found += '1'
		elif d[ele]>1:
			found += '2'
		else:
			found += '0'
	seq = found.split('0')
	total = 0
	print(seq)
	for ele in seq:
		if ele:
			if set(ele) == {'1'}:
				n = len(ele)
				total += (n*(n+1))//2
				total = total % M
				print(total)
			else:
				onec = ele.count('1')
				twoc = ele.count('2')
				odd_count = twoc//2+1 if twoc%2 else twoc//2
				if odd_count==1:
					total += onec
					total = total % M
				else:
					total += onec
					total += (odd_count)**2
					total = total % M
				print(total)
	print(total)