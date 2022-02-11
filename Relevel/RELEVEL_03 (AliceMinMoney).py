from itertools import combinations as co

def main():
	for _ in range(int(input())):
		N, M, F = map(int, input().split())
		C = {i: x for i,x in zip(range(N), list(map(int, input().split())))}
		A = {i: list(map(int, input().split())) for i in range(N)}
		
		all_combos = []
		for i in range(1,N+1):
			all_combos += list(co(range(N), i))

		totals = []
		for ele in all_combos:
			costs = [C[item] for item in ele]
			lists = [A[item] for item in ele]
			if min([sum(x) for x in zip(*lists)]) >= F:
				totals.append(sum(costs))
		# print(totals)
		print(min(totals, default = -1))

if __name__ == '__main__':
	main()