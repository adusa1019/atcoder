def solve(string):
    n, *h = map(int, string.split())
    curr = None
    for _h in h[::-1]:
        if curr is None:
            curr = _h
            continue
        if _h <= curr:
            curr = _h
            continue
        if _h - 1 == curr:
            continue
        return "No"
    return "Yes"


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
