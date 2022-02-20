def convert_to_float(num):
	for ele in num:
		if ele != '.' and ele.isdigit() == False:
			return False, False
	decimal_point_count = num.count('.')
	if decimal_point_count > 1:
		return False, False
	ans = 0
	decimal_point_position = num.find('.')
	if decimal_point_position == -1:
		n = len(num)
		for i in range(n):
			ans += int(num[n - i- 1]) * (10 ** i)
		ans = ans + 0.0
		return ans, True
	else:
		num_part_before_decimal = num[0:decimal_point_position]
		n = len(num_part_before_decimal)
		for i in range(n):
			ans += int(num_part_before_decimal[n - i - 1]) * (10 ** i)
		num_part_after_decimal = num[decimal_point_position+1:decimal_point_position+3]
		n = len(num_part_after_decimal)
		for i in range(n):
			ans += int(num_part_after_decimal[i]) * (10 ** -(i+1))
		ans = ans + 0.0
		return ans, True

def main():
	i = 0
	while True:
		if i == 0:
			num = input('\nPlease enter a positive float string: ')
		else:
			num = input('This is not a valid positive float string. Please re-enter a valid positive float string: ')
		ans, isFloat = convert_to_float(num)
		if isFloat:
			print(f'The float value of your string is: {ans:.2f}\nThe class of the converted output is: {type(ans)}')
			ip = input('Would you like to continue? (yes/no): ')
			if ip.lower() == 'no':
				break
			else:
				i = 0
		else:
			i+=1

if __name__ == '__main__':
	main()