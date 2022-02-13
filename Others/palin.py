def solve(s):
	n = len(s)
	for i in range(n//2):
		if s[i] != s[n-i-1]:
			print('Not a palindrome')
			return
	print('Palindrome')

def main():
	while True:
		s = input()
		solve(s)
		inp = input('Continue? Y/N:\n')
		if inp.lower()=='n':
			break

if __name__ == '__main__':
	main()