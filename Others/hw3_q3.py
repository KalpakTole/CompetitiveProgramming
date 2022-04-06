def inverse():
	S = input('\nEnter a list of integers separated by commas: ').strip().split(',')
	if len(S)<2:
		print('The entry is incorrect. Please enter a list that contains more than 1 element.\n')
		return
	for ele in S:
		print(f'The entry is: {ele}')
		try:
			ele = int(ele)
			try:
				print(f'The inverse of {ele} is {1/ele}')
			except:
				print(f'Oops! Exception <class "ZeroDivisionError"> occurred.')
		except:
			print(f'Oops! Exception <class "ValueError"> occurred.')
		

def main():
	inverse()
	while True:
		c = input('Do you want to continue? (yes/no): ')
		if c == 'yes' or c == 'y':
			inverse()
		elif c == 'no' or c == 'n':
			break

main()