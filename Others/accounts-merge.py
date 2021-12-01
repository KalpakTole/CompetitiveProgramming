class Solution:
    def accountsMerge(self, accounts):
        d = {}
        d[accounts[0][0]] = accounts[0][1:]
        print(f'{d=}')
        n = len(accounts)
        for i in range(1,n):
            print(i)
            val = set(accounts[i][1:])
            f = False
            for k,v in d.items():
                if set(v).intersection(val):
                    print(f'\n{v=}    {val=}')
                    f = True
                    d[k] = list(set(v).union(val))
                    break
            if not f:
                d[accounts[i][0]] = accounts[i][1:]
            print(f'{d=}')
            
        d = {k:v for k,v in sorted(d.items())}
        newarr = []
        for k,v in d.items():
            val = [k]+sorted(v)
            newarr.append(val)
        return newarr

