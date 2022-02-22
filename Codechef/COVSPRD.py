def main():
	for _ in range(int(input())):
		N,D = list(map(int, input().split()))
		if D<=10:
			ans = 2**D
			if ans>=N:
				print(N)
			else:
				print(ans)
			continue
		else:
			ans = 2**10
			iter = D-10
			f = False
			while iter<=D:
				if ans>=N:
					print(N)
					f = True
					break
				else:
					ans *= 3
		if f:
			if ans >= N:
				print(N)
			else:
				print(ans)

if __name__ == '__main__':
	main()