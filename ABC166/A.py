def solve(string):
    return "ABC" if "R" in string else "ARC"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
