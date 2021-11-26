import math

def SieveOfEratosthenes(n):
	prime = [True for i in range(n+1)]
	p = 2
	while (p * p <= n):
		if (prime[p] == True):
			for i in range(p * p, n+1, p):
				prime[i] = False
		p += 1
	sol = []
	for p in range(2, n+1):
		if prime[p]:
			sol.append(p)
	return sol

for _ in range(int(input())):
	X,Y = map(int, input().split())
	A = math.factorial(X)
	primes = SieveOfEratosthenes(A)
	for i in range(2,int(A**0.5)+1):
		if i not in primes:
			primes.append(i)
	primes.sort(reverse=True)
	ans = ''
	if len(primes)==0:
		ans = 'Chef'
		print(ans)
		continue
	elif primes[0] == A:
		ans = 'Chef'
		print(ans)
		continue
	co = 0
	flag = False
	while True:
		for ele in primes:
			if (A - ele) not in primes:
				co += 1
				D = ele
				A -= D
				flag = True
				break
		if A <= 0:
			if co%2==1:
				ans = 'Chef'
			else:
				ans = 'Divyam'
			break
		if flag == False:
			co += 1
			if co%2==1:
				ans = 'Chef'
			else:
				ans = 'Divyam'
			break
	print(ans)