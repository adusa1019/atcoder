def solve(string):
    if len(string) <= 2 and all([int(s) % 3 for s in [string, string[0], string[-1]]]):
        return "-1"
    *s, = map(lambda x: int(x) % 3, string)
    return str(2 - (sum(s) % 3 in s)) if sum(s) % 3 else "0"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
