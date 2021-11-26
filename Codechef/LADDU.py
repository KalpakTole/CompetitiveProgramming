for _ in range(int(input())):
	a,o = map(str, input().split())
	total_laddus = 0
	for i in range(int(a)):
		li = list(map(str, input().split()))
		if li[0]=='CONTEST_WON':
			total_laddus += 300
			if int(li[1]) < 20:
				total_laddus += 20 - int(li[1])
		elif li[0]=='TOP_CONTRIBUTOR':
			total_laddus += 300
		elif li[0]=='BUG_FOUND':
			total_laddus += int(li[1])
		elif li[0]=='CONTEST_HOSTED':
			total_laddus += 50
	if o=='INDIAN':
		print(total_laddus//200)
	else:
		print(total_laddus//400)