def solve(string):
    n, *xy = map(int, string.split())
    for i, (x1, y1) in enumerate(zip(*[iter(xy)] * 2)):
        k = set([])
        for j, (x2, y2) in enumerate(zip(*[iter(xy)] * 2)):
            if i >= j:
                continue
            _k = float("inf") if x1 == x2 else (y2 - y1) / (x2 - x1)
            if _k in k:
                return "Yes"
            else:
                k.add(_k)
    return "No"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
