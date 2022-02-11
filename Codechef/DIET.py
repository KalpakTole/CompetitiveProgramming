def main():
    for _ in range(int(input())):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        cur, f = 0, True
        for i in range(N):
            if cur + A[i] >= K:
                cur += A[i] - K
            else:
                print(f'NO {i+1}')
                f = False
                break
        if f:
            print('YES')


if __name__ == '__main__':
    main()
