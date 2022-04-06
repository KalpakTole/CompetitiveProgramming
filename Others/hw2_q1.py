def minmax():
	S = input('Please enter a list of numbers: ')
	S = S.replace(',', ' ')
	S = S.replace(';', ' ')
	S = S.replace(':', ' ')
	S = S.replace('/', ' ')
	S = S.replace('.', ' ')
	nums = S.split()
	nums = list(map(int, nums))
	print(f'Minimum number is: {min(nums)}')
	print(f'Maximum number is: {max(nums)}')

def main():
	minmax()
	while True:
		c = input('Would you like to continue? (yes/no): ')
		if c == 'yes' or c == 'y':
			minmax()
		elif c == 'no' or c == 'n':
			break

main()