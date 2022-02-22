def main():
	for _ in range(int(input())):
		N,X,Y = list(map(int, input().split()))
		if (not X%2 and not Y%2) or (X%2 and Y%2):
			print(0)
		else:
			print(1)		

if __name__ == '__main__':
	main()