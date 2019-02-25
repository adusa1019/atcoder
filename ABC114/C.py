from math import ceil, log10
from itertools import product


def solve(string):
    n = int(string)
    ans = 0
    for i in range(3, ceil(log10(n)) + 1):
        tmp = (int("".join(x))
               for x in product("753", repeat=i)
               if "7" in x and "5" in x and "3" in x)
        ans += len([x for x in tmp if x <= n])
    return str(ans)


if __name__ == '__main__':
    print(solve(input()))
