for _ in range(int(input())):
	N = int(input())
	S = input()
	ah,am,bh,bm=0,0,0,0
	ans = 0
	for i in range(0,2*N,2):
		if S[i]=='1':
			ah+=1
		elif S[i]=='0':
			am+=1
		if ah+bm>N or am+bh>N:
			ans = i+1
			break
		if S[i+1]=='0':
			bm+=1
		elif S[i+1]=='1':
			bh+=1
		if am+bh>N or ah+bm>N:
			ans = i+2
			break
	if ans==0:
		print(2*N)
	else:
		print(ans)