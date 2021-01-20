def solve(string):
    return string + "es" if string[-1] == "s" else string + "s"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
