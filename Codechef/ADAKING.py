def main():
	for _ in range(int(input())):
		K = int(input())
		S = 'O' + ('.' * (K-1))
		S += 'X' * (64-K)
		newS = ''
		for i in range(64):
			if i and not i % 8:
				newS += '\n'
				newS += S[i]
			else:
				newS += S[i]
		print(newS)

if __name__ == '__main__':
	main()