def main():
	for _ in range(int(input())):
		Z,Y,A,B,C = list(map(int, input().split()))
		if (Z-Y)>=(A+B+C):
			print('YES')
		else:
			print('NO')		

if __name__ == '__main__':
	main()