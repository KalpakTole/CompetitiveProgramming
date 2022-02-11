def main():
    for _ in range(int(input())):
        S = input()
        li = list(map(int, S[1:-1].split(',')))
        print(sum(set(li)))


if __name__ == '__main__':
    main()
