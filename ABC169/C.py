def solve(string):
    a, b = string.split()
    b = "".join(b.split("."))
    return str(int(a) * int(b) // 100)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
