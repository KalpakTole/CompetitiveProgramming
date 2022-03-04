def main():
	for _ in range(int(input())):
		N,M = list(map(int, input().split()))
		R = list(map(int, input().split()))
		arr = [0 for i in range(N)]
		for i in range(M):
			new_arr = [x for x in range(R[i],-1,-1)]
			new_arr += [x for x in range(1,N-R[i])]
			arr = [max(a,b) for a,b in zip(arr,new_arr)]
		print(*arr)
		

if __name__ == '__main__':
	main()