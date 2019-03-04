def solve(string):
    s, k = string.split()
    for _s in s[:int(k)]:
        if _s != "1":
            return _s
    else:
        return "1"


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
