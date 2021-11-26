for _ in range(int(input())):
    N,X,p,k = list(map(int, input().split()))
    A = list(map(int, input().split()))
    c = 0
    A.sort()
    for i in range(N):
        A[k-1] = X
        c += 1
        A.sort()
        if A[p-1] == X:
            print(c)
            break
    if c==N:
        print(-1)
