noe = int(input('Enter number of equations: '))
nov = int(input('Enter number of variables: '))
# 2 2
var = {}
for i in range(noe):
	for j in range(nov):
		a = int(input(f'Enter coefficient {j+1} of equation {i+1}: '))
		var[i+1] = var.get(i+1,[]) + [a]
	a = int(input(f'Enter RHS for equation {i+1}: '))
	var[i+1] = var.get(i+1,[]) + [a]

# print(var)
ss = []
solset = []
if nov == 2:
	a = var[1]
	for i in range(-100,100):
		for j in range(-100,100):
			if a[0]*i + a[1]*j == a[2]:
				ss.append([i,j])
	del var[1]
	for k,v in var.items():
		for i in ss:
			if i[0]*v[0] + i[1]*v[1] == v[2]:
				solset.append(tuple(i))
	solset = set(solset)
# print(solset)
if nov == 3:
	a = var[1]
	for i in range(-100,100):
		for j in range(-100,100):
			for k in range(-100,100):
				if a[0]*i + a[1]*j +a[2]*k == a[3]:
					ss.append([i,j,k])
	# print(ss)
	del var[1]
	for k,v in var.items():
		for i in ss:
			if i[0]*v[0] + i[1]*v[1] + i[2]*v[2] == v[3]:
				solset.append(tuple(i))
	solset = set(solset)
# print(solset)
if nov == 4:
	a = var[1]
	for i in range(-100,100):
		for j in range(-100,100):
			for k in range(-100,100):
				for l in range(-100,100):
					if a[0]*i + a[1]*j +a[2]*k +a[3]*l == a[4]:
						ss.append([i,j,k,l])
	del var[1]
	for k,v in var.items():
		for i in ss:
			if i[0]*v[0] + i[1]*v[1] + i[2]*v[2] + i[3]*v[3] == v[4]:
				solset.append(tuple(i))
	solset = set(solset)

solset = sorted(list(solset))
print('\nSolutions:\n')
print(solset)
print(f'\nLength: {len(solset)}\n')
