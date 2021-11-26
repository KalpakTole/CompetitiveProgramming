for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    co,ca,i = 0,0,0
    flag = False
    while i<n:
        if Q[i]+ca >= k:
            ca += Q[i] - k
            co += 1
        else:
            print(co+1)
            flag = True
            break
        i+=1
    if flag==False:
        co = co + (ca//k) + 1
        print(co)