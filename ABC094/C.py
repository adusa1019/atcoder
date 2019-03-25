def solve(string):
    n, *x = map(int, string.split())
    mid = n // 2
    l, r = sorted(x)[mid - 1:mid + 1]
    return "\n".join([str(r) if _x < r else str(l) for _x in x])


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
