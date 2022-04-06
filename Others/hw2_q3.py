def sent_dict(S,d):
	for ele in S:
		if ele.lower() in d:
			d[ele.lower()] += 1
	print('Your sentence dictionary:')
	for k,v in d.items():
		if v!=0:
			if v==1:
				print(f"Letter '{k}' appears {v} time.")
			else:
				print(f"Letter '{k}' appears {v} times.")


def main():
	d = {chr(i): 0 for i in range(97, 97+26)}
	S = input('Please enter a sentence: ')
	sent_dict(S,d)
	while True:
		c = input('Would you like to continue? (yes/no): ')
		if c == 'yes' or c == 'y':
			d = {chr(i): 0 for i in range(97, 97+26)}
			S = input('Please enter a sentence: ')
			sent_dict(S,d)
		elif c == 'no' or c == 'n':
			break

main()