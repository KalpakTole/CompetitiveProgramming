from collections import Counter as co


def main():
    for _ in range(int(input())):
        N = int(input())
        A = list(map(int, input().split()))
        if N == 1:
            print(0)
        elif N == 2:
            if len(set(A)) == 1:
                print(0)
            else:
                print(-1)
        else:
            d = co(A)
            m = max(d.values())
            if m > 1:
                print(N - m + 1)
            else:
                print(-1)


if __name__ == '__main__':
    main()
