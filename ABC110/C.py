def solve(string):
    s, t = string.split()

    c_s = sorted([s.count(_c) for _c in set(s)])
    c_t = sorted([t.count(_c) for _c in set(t)])

    if c_s == c_t:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
