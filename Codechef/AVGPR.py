def main():
	for _ in range(int(input())):
		N = int(input())
		A = list(map(int, input().split()))
		co = 0
		for i in range(N-1):
			for j in range(i+1,N):
				val = (A[i] + A[j])/2
				if val in A:
					co += 1
		print(co)

if __name__ == '__main__':
	main()
	