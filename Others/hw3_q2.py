f1 = open('input.txt', 'r')
text = f1.readlines()
f1.close()

nums = []
answer = ''
f3 = open('output.txt', 'w+')

for line in text:
	line = line.strip()
	try:
		num = float(line)
		nums.append(num)
	except:
		answer += f'{line}. '
f3.write(f'Number of numerical values in the file is:\n{len(nums)}\n\n')
f3.write(f'The average of numerical values in the file is:\n{sum(nums)/len(nums)}\n\n')
f3.write(f'The concatenated text in the file is:\n{answer}\n\n')
f3.write(f'The length of concatenated text in the file is:\n{len(answer)}')
f3.close()