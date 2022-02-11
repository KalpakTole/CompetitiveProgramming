def main():
	for _ in range(int(input())):
		N = int(input())
		S = input()
		ei = N-1
		co,mco = 0,0
		for i in range(N):
			if S[i]=='P':
				co += 1
			else:
				if co>mco:
					mco=co
					ei = i-1
				co = 0
		if co>mco:
			mco = co
			ei = N-1
		p1 = S[:ei-mco+1]
		p1nos = [x for x in range(len(p1)-1,-1,-1)]
		p1nosps = [p1nos[i] for i in range(len(p1)) if p1[i] == 'P']

		p2 = S[ei+1:]
		p2nos = [x for x in range(len(p2))]
		p2nosps = [p2nos[i] for i in range(len(p2)) if p2[i] == 'P']

		total1, total2 = 0, 0
		lp1,lp2 = len(p1nosps), len(p2nosps)
		for i in range(lp1):
			total1 += p1nosps[i] - (lp1 - (i+1))
		for i in range(lp2):
			total2 += p2nosps[i] - i

		# print(f'{ei=}')
		# print(f'{mco=}')
		# print(f'{p1=}')
		# print(f'{p1nos=}')
		# print(f'{p1nosps=}')
		# print(f'{p2=}')
		# print(f'{p2nos=}')
		# print(f'{p2nosps=}')
		# print(f'{total1=}')
		# print(f'{total2=}')
		print(f'{total1+total2=}')


if __name__ == '__main__':
	main()