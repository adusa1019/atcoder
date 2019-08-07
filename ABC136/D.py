def solve(string):
    n = len(string)

    def op(string, ans, forward=True):
        count = 0
        check, sign, base = ("R", 1, 0) if forward else ("L", -1, n - 1)
        for i, a in enumerate(string[::sign]):
            if a == check:
                count += 1
            elif count > 0:
                ans[base + sign * i] += count // 2
                ans[base + sign * (i - 1)] += (count + 1) // 2
                count = 0
        return ans

    ans = op(string, [0] * n, True)
    return " ".join([str(a) for a in op(string, ans, False)])


if __name__ == '__main__':
    print(solve(input()))
