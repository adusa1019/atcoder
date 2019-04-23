from functools import lru_cache


def solve(string):
    h, w, k = map(int, string.split())
    c = [1, 1]
    for _ in range(1, 7):
        i, j = c[-2:]
        c.append(i + j)

    @lru_cache(h * w)
    def rec(pos, depth):
        if depth == h:
            return 1 if pos == 1 else 0
        ans = rec(pos, depth + 1) * c[pos - 1] * c[w - pos]
        if pos < w:
            ans += rec(pos + 1, depth + 1) * c[pos - 1] * c[w - pos - 1]
        if pos > 1:
            ans += rec(pos - 1, depth + 1) * c[pos - 2] * c[w - pos]
        return ans

    return str(rec(k, 0) % (10**9 + 7))


if __name__ == '__main__':
    print(solve(input()))
