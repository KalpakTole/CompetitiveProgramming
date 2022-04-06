
class DefaultException(Exception):
	def __str__(self):
		return 'Caught a python exception.'

class Type1Error(Exception):
	def __str__(self):
		return 'Caught a user-defined <Type 1> exception.'


class Type2Error(Exception):
	def __str__(self):
		return 'Caught a user-defined <Type 2> exception.'
	

def is_letter_present(S):
	for ele in S:
		if ele.isalpha():
			return True
	return False


def is_special_present(S):
	special_chars = ['!','*','$','&','@','#','%','^']
	for ele in S:
		if ele in special_chars:
			return True
	return False


def custom_abs():
	S = input('\nPlease enter a number: ').strip()
	while True:
		try:
			S = S.replace('-', '')
			S = S.replace('+', '')
			S = float(S)
			print(f'The absolute value of your number is: {S}')
			return
		except:
			try:
				letter = is_letter_present(S)
				special = is_special_present(S)
				if letter and special:
					raise Type2Error
				if special:
					raise Type1Error
				if letter:
					raise DefaultException
			except Type2Error as e:
				S = input(f'{e} Please re-enter a valid number: ')
			except Type1Error as e:
				S = input(f'{e} Please re-enter a valid number: ')
			except DefaultException as e:
				S = input(f'{e} Please re-enter a valid number: ')
		

def main():
	custom_abs()
	while True:
		c = input('Would you like to continue? (yes/no): ')
		if c == 'yes' or c == 'y':
			custom_abs()
		elif c == 'no' or c == 'n':
			break


main()
