def main():
	for _ in range(int(input())):
		N = int(input())
		d = {}
		for i in range(N):
			S = input()
			d[S] = d.get(S, 0) + 1
		if len(d)>1 and len(set(d.values())) == 1:
			print('Draw')
		else:
			print(max(d, key=lambda x:x[1], default='Draw'))

if __name__ == '__main__':
	main()