def main():
	for _ in range(int(input())):
		N = int(input())
		A = list(map(int, input().split()))
		total = sum(A)
		curr = A[0]
		cumu_A = [curr]
		for i in range(1,N):
			curr += A[i]
			cumu_A.append(curr)
		mi = total
		for i in range(N):
			val = max(cumu_A[i], total-cumu_A[i])
			if val < mi:
				mi = val
		print(mi)

if __name__ == '__main__':
	main()