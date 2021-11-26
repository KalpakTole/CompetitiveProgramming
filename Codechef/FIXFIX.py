for _ in range(int(input())):
	n,k = map(int, input().split())
	li = [x for x in range(1,n+1)]
	if k==n:
		print(*li)
	elif k==1 and n==2:
		print(-1)
	else:
		newli = li[:k]+li[k:][::-1]
		print(*newli)