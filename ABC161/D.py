from itertools import product


def solve(string):
    k = int(string)
    if k < 10:
        return str(k)

    t = [[0] * 12 for _ in range(10)]
    t[0] = [0] + [1] * 10 + [0]
    ac = 9
    for i, j in product(range(1, 10), range(1, 11)):
        t[i][j] = t[i - 1][j - 1] + t[i - 1][j] + t[i - 1][j + 1]
        ac += t[i][j] if j > 1 else 0
        if ac >= k:
            k -= ac - t[i][j]
            break
    ans = str(j - 1)
    while i > 0:
        i -= 1
        j -= 1
        tmp = t[i][j]
        while tmp < k:
            j += 1
            tmp += t[i][j]
        k -= tmp - t[i][j]
        ans += str(j - 1)
    return ans


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
