def solve(string):
    *nkrsp, t = string.split()
    t = list(t)
    n, k, *rsp = map(int, nkrsp)
    b = {k: v for k, v in zip("spr", rsp)}
    ans = sum([b[k] for k in t[:k]])
    for i, _t in enumerate(t[k:]):
        if _t == t[i]:
            t[i + k] = "x"
        else:
            ans += b[_t]
    return str(ans)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
