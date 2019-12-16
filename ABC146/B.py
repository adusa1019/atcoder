def solve(string):
    n, s = string.split()
    b = ord("A")
    return "".join([chr(((ord(_s) - b + int(n)) % 26) + b) for _s in s])


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
