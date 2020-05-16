def solve(string):
    return "Yes" if "7" in string else "No"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
