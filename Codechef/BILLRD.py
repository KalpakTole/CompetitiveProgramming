for _ in range(int(input())):
	N,K,x,y = map(int, input().split())
	if x==y:
		print(N,N)
		continue
	if x>y:
		y+=(N-x)
		x=N
	else:
		x+=(N-y)
		y=N
	first_point = (x,y)
	if x==N:
		clockwise = False
	elif y==N:
		clockwise = True
	if clockwise == False:
		x,y=y,x
		second_point = (x,y)
		y-=x
		x=0
		third_point = (x,y)
		x,y=y,x
		fourth_point = (x,y)
	else:
		x,y=y,x
		second_point = (x,y)
		x-=y
		y=0
		third_point = (x,y)
		x,y=y,x
		fourth_point = (x,y)
	if K%4==1:
		print(*first_point)
	elif K%4==2:
		print(*second_point)
	elif K%4==3:
		print(*third_point)
	elif K%4==0:
		print(*fourth_point)