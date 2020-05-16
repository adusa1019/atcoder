def solve(string):
    i, c = 0, 100
    while c < int(string):
        i += 1
        c = c * 1.01 // 1
    return str(i)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
