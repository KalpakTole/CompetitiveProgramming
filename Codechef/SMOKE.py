import math
def main():
	for _ in range(int(input())):
		N,X,Y = list(map(int, input().split()))
		iter = N//100
		if iter > 0:
			if X <= 25 * Y:
				ans = iter * X
				if X <= math.ceil((N % 100)/4) * Y:
					ans += X
				else:
					ans += math.ceil((N % 100)/4) * Y
			else:
				ans = iter * 25 * Y
				ans += math.ceil((N % 100)/4) * Y
		else:
			carpoll = math.ceil(N/4) * Y
			if X <= carpoll:
				ans = X
			else:
				ans = carpoll
		print(ans)		

if __name__ == '__main__':
	main()