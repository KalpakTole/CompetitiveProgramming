import math

def main():
	for _ in range(int(input())):
		N,M = list(map(int, input().split()))
		print(int(math.ceil(N/2)*math.ceil(M/2)))
		

if __name__ == '__main__':
	main()