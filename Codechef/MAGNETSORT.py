def main():
	for _ in range(int(input())):
		N = int(input())
		A = list(map(int, input().split()))
		P = input()
		if sorted(A) == A:
			print(0)
		elif set(P) == {'N'} or set(P) == {'S'}:
			print(-1)
		elif P[0] != P[-1]:
			print(1)
		else:
			fN,fS,lN,lS = P.find('N'),P.find('S'),P.rfind('N'),P.rfind('S')
			if (sorted(A[fN:lS+1])+A[lS+1:]) == A or (A[:fS]+sorted(A[fS:lN+1])) == A:
				print(1)
			else:
				print(2)
			print(fN, fS, lN, lS)

if __name__ == '__main__':
	main()