def implementAPI(logs):
	d = {}
	res = []
	for log in logs:
		terms = log.split()
		if terms[0] == 'register':
			if terms[1] in d:
				ans = 'Username already exists'
			else:
				d[terms[1]] = [terms[2], 0]
				ans = 'Registered Successfully'
		elif terms[0] == 'login':
			if terms[1] in d:
				if terms[2] == d[terms[1]][0]:
					if d[terms[1]][1] == 0:
						d[terms[1]][1] = 1
						ans = 'Logged In Successfully'
					else:
						ans = 'Login Unsuccessful'
				else:
					ans = 'Login Unsuccessful'
			else:
				ans = 'Login Unsuccessful'
		elif terms[0] == 'logout':
			if terms[1] in d:
				if d[terms[1]][1] == 1:
					d[terms[1]][1] = 0
					ans = 'Logged Out Successfully'
				else:
					ans = 'Logout Unsuccessful'
			else:
				ans = 'Logout Unsuccessful'
		res.append(ans)
	return res


def main():
    for _ in range(1):
        logs = ['register david david123', 'register adam 1Adam1', 'login david david123', 'login adam 1adam1', 'logout david']
        ans = implementAPI(logs)
        print(ans)


if __name__ == '__main__':
    main()
