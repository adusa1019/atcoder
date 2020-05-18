def solve(string):
    k, s = string.split()
    k = int(k)
    return s if len(s) <= k else s[:k] + "..."


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
