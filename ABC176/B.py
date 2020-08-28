def solve(string):
    return "Yes" if sum(map(int, list(string))) % 9 == 0 else "No"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
