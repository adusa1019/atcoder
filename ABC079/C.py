from itertools import product


def solve(string):
    s = [0] * 7
    for i, _s in enumerate(string):
        s[2 * i] = _s
    for op in product("+-", repeat=3):
        for i, o in enumerate(op):
            s[2 * i + 1] = o
        if eval("".join(s)) == 7:
            return "".join(s) + "=7"


if __name__ == '__main__':
    print(solve(input()))
