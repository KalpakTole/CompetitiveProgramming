import copy
def main():
	for _ in range(int(input())):
		N = int(input())
		H = list(map(int, input().split()))
		co = 0
		prevH = copy.deepcopy(H)
		for i in range(N//2):
			p1 = H[:N//2]
			if N % 2:
				p2 = H[N//2+1:]
			else:
				p2 = H[N//2:]
			p2 = p2[::-1]
			if p1==p2:
				break
			H = [p1[i] if x==p2[i] else x for x in H]
			if prevH != H:
				co += 1
			prevH = copy.deepcopy(H)
			# print(p1,p2)
			# print(H)
		print(co)

if __name__ == '__main__':
	main()