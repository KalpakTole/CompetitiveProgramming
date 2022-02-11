def main():
    for _ in range(int(input())):
        N, P, Q = list(map(int, input().split()))
        A = list(map(int, input().split()))
        A.sort()
        for i in range(N):
            if Q > 0:
                val = A[i]//2
                if Q >= val:
                    A[i] = A[i] - 2*val
                    Q = Q - val
                else:
                    A[i] = A[i] - 2*Q
                    Q = 0
            else:
                break
        A.sort()
        for i in range(N):
            if P > 0:
                if A[i] != 0:
                    if P >= A[i]:
                        P = P - A[i]
                        A[i] = 0
                    else:
                        break
                else:
                    continue
            else:
                break
        print(A.count(0))


if __name__ == '__main__':
    main()
