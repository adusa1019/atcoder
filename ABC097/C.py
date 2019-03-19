def solve(string):
    s, k = string.split()
    k = int(k)
    chars = sorted(set(s))
    exists = []

    def dfs(base):
        exists.append(base)
        if len(exists) >= k:
            return
        for c in chars:
            if base + c in s:
                dfs(base + c)

    for c in chars[:3]:
        dfs(c)

    return exists[k - 1]


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
