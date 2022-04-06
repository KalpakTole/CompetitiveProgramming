def pizza_hut(location, toppings, d):
	toppings_available = d[location]
	if set(toppings).issubset(set(toppings_available)):
		print('The toppings you provided for your pizza are all available. Please proceed to checkout.')
	else:
		toppings_not_available = set(toppings) - set(toppings_available)
		if len(toppings_not_available) == len(toppings):
			print('Based on your location, none of the toppings are available.')
		else:
			print('Based on your location, the following toppings are not available: ',end='')
			print(*toppings_not_available, sep=', ')


def main():
	d = {'Dallas': ['mushroom', 'spinach', 'onion', 'tomato', 'feta'],
		 'Austin': ['bacon', 'tomato', 'eggplant', 'olive', 'cheddar'],
		'Houston': ['chicken', 'pineapple', 'spinach', 'olive', 'steak']}
	location = input('Please enter your location: ')
	toppings = input('Please enter the toppings of your pizza: ').split(', ')
	pizza_hut(location, toppings, d)
	while True:
		c = input('Do you want to continue? (yes/no): ')
		if c == 'yes' or c == 'y':
			location = input('Please enter your location: ')
			toppings = input('Please enter the toppings of your pizza: ').split(', ')
			pizza_hut(location, toppings, d)
		elif c == 'no' or c == 'n':
			break


main()
