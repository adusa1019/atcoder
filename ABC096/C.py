def solve(string):
    h, w, *s = string.split()
    h = int(h)
    w = int(w)
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                continue
            check = False
            if i > 0:
                check |= s[i][j] == s[i - 1][j]
            if i < h - 1:
                check |= s[i][j] == s[i + 1][j]
            if j > 0:
                check |= s[i][j] == s[i][j - 1]
            if j < w - 1:
                check |= s[i][j] == s[i][j + 1]
            if not check:
                return "No"
    return "Yes"


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve('{} {}\n'.format(n, m) + '\n'.join([input() for _ in range(n)])))
