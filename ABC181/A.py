def solve(string):
    return "Black" if int(string) % 2 else "White"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
