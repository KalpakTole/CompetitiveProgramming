def main():
    for _ in range(int(input())):
        K = int(input())
        if K == 1:
            print(1, 1)
            continue
        d = {}
        for i in range(1, K//2+1):
            if not K % i:
                b = i
                a = K//i
                # store lcm of a,b and value of a in a dictionary with key as lcm and value as max(all a's for that key)
                if a == b or not a % b:
                    lcm = a
                elif not b % a:
                    lcm = b
                else:
                    lcm = a*b
                if d.get(lcm):
                    d[lcm] = max(a, d[lcm])
                else:
                    d[lcm] = a
        # print(d)
        d = sorted(d.items())
        a = d[0][1]
        b = K//a
        print(a, b)


if __name__ == '__main__':
    main()
