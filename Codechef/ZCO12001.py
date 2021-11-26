N = int(input())
S = list(map(int, input().split()))
co,bestco = 0,0
matco, bestmatco = 0,0
prevcozeropos = 0
curcozeropos = 0
for i in range(N):
	if S[i] == 1:
		co += 1
		if co > bestco:
			bestco = co
			bestpos = i+1
	elif S[i] == 2:
		co -= 1
	if co != 0:
		matco += 1
	elif co==0:
		curcozeropos = prevcozeropos
		prevcozeropos = i
		if matco > bestmatco:
			bestmatco = matco + 1
			bestmatpos = curcozeropos+2
		matco = 0
print(bestco, bestpos, bestmatco, bestmatpos)