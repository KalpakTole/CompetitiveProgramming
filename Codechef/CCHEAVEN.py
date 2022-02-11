def main():
    for _ in range(int(input())):
        L = int(input())
        S = input()
        gy, by = 0, 0
        ans = 'NO'
        for i in range(L):
            if S[i] == '1':
                gy += 1
            else:
                by += 1
            if gy >= by:
                ans = 'YES'
                break
        print(ans)


if __name__ == '__main__':
    main()
