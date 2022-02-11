def main():
    for _ in range(int(input())):
        N, M = list(map(int, input().split()))
        if N == M:
            print(2*(N+1))
            print('01'*(N+1))
        elif N > M:
            ans = '0' + '10'*M + '1' + '0' + (N-(M+1))*'010'
            print(len(ans))
            print(ans)
        else:
            ans = '1' + '01'*N + '0' + '1' + (M-(N+1))*'101'
            print(len(ans))
            print(ans)


if __name__ == '__main__':
    main()
