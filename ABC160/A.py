def solve(string):
    return "Yes" if string[2] == string[3] and string[4] == string[5] else "No"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
