def solve(s):
    n = len(s) // 2
    return str(sum(s0 != s1 for s0, s1 in zip(s[:n], s[::-1][:n])))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
