def atm(amount, d):
	for k in d.keys():
		if amount >= k:
			val = amount // k
			amount -= val*k
			d[k] = val
	for k,v in d.items():
		print(f'Denomination $: {k}\t\tNumber of notes {v}')
		
def main():
	d = {100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}
	amount = float(input('Enter Amount to be paid in $: '))
	while amount != int(amount):
		amount = float(input(
			'This is not a valid positive integer value. Please re-enter a valid positive integer: '))
	amount = int(amount)
	atm(amount, d)
	while True:
		c = input('Would you like to continue? (yes/no): ')
		if c == 'yes' or c == 'y':
			d = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
			amount = int(input('Enter Amount to be paid in $: '))
			atm(amount, d)
		elif c == 'no' or c == 'n':
			break

main()
