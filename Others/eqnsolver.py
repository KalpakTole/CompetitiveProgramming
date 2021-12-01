x,y,z = map(int, input('Enter space-separated coeffecients of x, y and z: ').split())
N = int(input('Enter RHS of your equation: '))
print('Solutions:')
m = 0
for i in range(100):
	for j in range(100):
		for k in range(100):
			if (x*i + y*j + z*k) == N:
				print(f'Solution {m}: x = {i}, y = {j}, z = {k}')
				m += 1
if m == 0:
	print('No Solution found!')