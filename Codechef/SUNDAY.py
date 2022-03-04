def main():
	holidays = [6,7,13,14,20,21,27,28]
	for _ in range(int(input())):
		count = 8
		N = int(input())
		A = list(map(int, input().split()))
		for day in A:
			if day not in holidays:
				count += 1
		print(count)		

if __name__ == '__main__':
	main()