def minimumKeypadClickCount(S):
	d = {}
	for ele in S:
		d[ele] = d.get(ele,0) + 1
	d = {k:v for k,v in sorted(d.items(), key=lambda x:x[1], reverse=True)}
	li = list(d.items())
	ans = 0
	for i in range(len(li)):
		mul = i//9+1
		ans += li[i][1] * mul
	return ans


def main():
	for _ in range(1):
		# S = 'abacadefghibj'
		S = 'abcghdiefjoba'
		ans = minimumKeypadClickCount(S)
		print(ans)
		

if __name__ == '__main__':
	main()