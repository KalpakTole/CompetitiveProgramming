for _ in range(int(input())):
	N = int(input())
	H = list(map(int, input().split()))
	if N%2==0 or H[0]!=1:
		print('no')
	elif H[:N//2] == H[::-1][:N//2]:
		val = (N//2)
		if sum(H[:N//2]) == val*(val+1)//2:
			print('yes')
		else:
			print('no')
	else:
		print('no')