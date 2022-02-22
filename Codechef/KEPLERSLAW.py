def main():
	for _ in range(int(input())):
		T1,T2,R1,R2 = list(map(int, input().split()))
		if (T1**2/R1**3) == (T2**2/R2**3):
			print('YES')
		else:
			print('NO')

if __name__ == '__main__':
	main()