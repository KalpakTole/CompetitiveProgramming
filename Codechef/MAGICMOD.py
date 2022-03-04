def main():
	for _ in range(int(input())):
		N = int(input())
		A = list(map(int, input().split()))
		to_make = [i for i in range(1,N+1)]
		if set(A) == set(to_make):
			print('YES',N+1)
		elif len(set(A)) != N:
			print('NO')
		else:
			mi = N+1
			A.sort()
			for i in range(N):
				if A[i] > N:
					ma = A[i]
					ma_ind = i
					break
			rem_nos = set(A[ma_ind:])
			rem_nos_to_make = set(to_make[ma_ind:])
			flag = False
			for i in range(mi,ma):
				if rem_nos_to_make == set([x%i for x in rem_nos]):
					print('YES',i)
					flag = True
					break
			if flag == False:
				print('NO')

if __name__ == '__main__':
	main()