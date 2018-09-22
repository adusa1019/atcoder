def gcd(numbers):
    _min = numbers[0]
    tmp = sorted([_n % _min for _n in numbers])
    return _min if tmp[-1] == 0 else gcd(sorted([_t if _t > 0 else _min for _t in tmp]))


def solve(string):
    ins = string.split("\n")
    n, x = map(int, ins[0].split(" "))
    xs = list(map(int, ins[1].split(" ")))
    xs.append(x)
    xs = sorted(xs)
    diff = [_n - _p for _p, _n in zip(xs, xs[1:])]
    return str(gcd(diff))


if __name__ == '__main__':
    tmp = [input(), input()]
    print(solve('\n'.join(tmp)))
