def solve(string):
    n, t, *ct = map(int, string.split())
    c = [_c for _c, _t in zip(ct[::2], ct[1::2]) if _t <= t]
    return str(min(c)) if len(c) else "TLE"


if __name__ == '__main__':
    n, t = map(int, input().split())
    print(solve("{} {}\n".format(n, t) + "\n".join([input() for _ in range(n)])))
