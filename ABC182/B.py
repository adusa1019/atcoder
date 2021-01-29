def solve(string):
    n, *a = map(int, string.split())
    return str(max(t := {i: sum([not v % i for v in a]) for i in range(2, max(a) + 1)}, key=t.get))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
