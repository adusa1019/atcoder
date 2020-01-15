def solve(string):
    k, x = map(int, string.split())
    return "Yes" if k * 500 >= x else "No"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
