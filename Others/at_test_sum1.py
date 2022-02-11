def countMax(upRight):
	rows = []
	cols = []
	for ele in upRight:
		r, c = map(int, ele.split())
		rows.append(r)
		cols.append(c)
	mr = min(rows)
	mc = min(cols)
	return mr*mc


def main():
	for _ in range(1):
		upRight = ['1 4','2 3','4 1']
		# upRight = ['2 3', '3 7', '4 1']
		ans = countMax(upRight)
		print(ans)


if __name__ == '__main__':
	main()
