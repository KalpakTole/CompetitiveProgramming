for _ in range(int(input())):
    N,K,X,Y = list(map(int, input().split()))
    ini =  X
    while X!=Y:
        X = (X+K)%N
        if ini == X:
            break
    if X==Y:
        print('YES')
    else:
        print('NO')