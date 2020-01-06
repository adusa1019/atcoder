def solve(string):
    x = int(string)
    for i in range(x, 2 * x):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            return str(i)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
