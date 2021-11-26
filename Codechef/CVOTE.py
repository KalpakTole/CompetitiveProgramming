N,M = map(int, input().split())
chefs, countries, d = {}, {}, {}
for i in range(N):
	na,co = map(str, input().split())
	d[na] = co
for i in range(M):
	ch = input()
	chefs[ch] = chefs.get(ch, 0) + 1
	countries[d[ch]] = countries.get(d[ch], 0) + 1

cod,chd = {},{}
for k,v in countries.items():
	cod[v] = cod.get(v, []) + [k]
for k,v in chefs.items():
	chd[v] = chd.get(v, []) + [k]

print(min(cod[max(cod.keys())]))
print(min(chd[max(chd.keys())]))