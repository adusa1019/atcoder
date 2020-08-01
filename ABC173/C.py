from itertools import product


def solve(string):
    h, w, k, *c = string.split()
    h, w, k = map(int, [h, w, k])
    ans = 0
    for f in product([True, False], repeat=h + w):
        count = 0
        for _f, _c in zip(f, c):
            if _f:
                continue
            count += sum(1 if __f and v == "#" else 0 for __f, v in zip(f[h:], _c))
        ans += 1 if count == k else 0
    return str(ans)

    pass


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
