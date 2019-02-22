def collatz(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1


def solve(string):
    s = int(string)
    checks = set([])
    for _ in range(10**6):
        if s in checks:
            break
        else:
            checks.add(s)
            s = collatz(s)
    return str(len(checks) + 1)


if __name__ == '__main__':
    print(solve(input()))
