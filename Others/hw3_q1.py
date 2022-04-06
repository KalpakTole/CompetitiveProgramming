f1 = open('numbers.txt','r')
f2 = open('operators.txt','r')
f3 = open('output.txt','w+')
# operator_position = 0
operator = f2.readline().strip()
while True:
	num1 = f1.readline().strip()
	num2 = f1.readline().strip()
	error_type = None
	try:
		num1 = int(num1)
		num2 = int(num2)
	except Exception as e:
		error_type = 'ValueError'
	if not num1 and not num2:
		break
	if operator == '+':
		if error_type:
			line_to_write = f'{num1} {operator} {num2} - Addition cannot be performed (ValueError)\n'
		else:
			line_to_write = f'{num1} {operator} {num2} = {num1+num2}\n'
	elif operator == '-':
		if error_type:
			line_to_write = f'{num1} {operator} {num2} - Subtraction cannot be performed (ValueError)\n'
		else:
			line_to_write = f'{num1} {operator} {num2} = {num1-num2}\n'
	elif operator == '*':
		if error_type:
			line_to_write = f'{num1} {operator} {num2} - Multiplication cannot be performed (ValueError)\n'
		else:
			line_to_write = f'{num1} {operator} {num2} = {num1*num2}\n'
	elif operator == '/':
		if error_type:
			line_to_write = f'{num1} {operator} {num2} - Division cannot be performed (ValueError)\n'
		else:
			try:
				line_to_write = f'{num1} {operator} {num2} = {num1/num2}\n'
			except:
				error_type = 'ZeroDivisionError'
				line_to_write = f'{num1} {operator} {num2} - Division by zero not allowed (ZeroDivisionError)\n'
	f3.write(line_to_write)
	if error_type == None:
		operator = f2.readline().strip()

f1.close()
f2.close()
f3.close()