def solve(string):
    s, t = string.split()
    return str(sum([_s == _t for _s, _t in zip(s, t)]))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
