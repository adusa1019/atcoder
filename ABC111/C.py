import collections


def solve(string):
    n, *v = map(int, string.split())
    if len(set(v)) == 1:
        return str(n // 2)
    else:
        odds = v[1::2]
        _o = collections.Counter(odds)
        r_o = {str(v): k for k, v in _o.items()}
        evens = v[::2]
        _e = collections.Counter(evens)
        r_e = {str(v): k for k, v in _e.items()}
        ans1 = 0
        tmp = max(_o.values())
        ans1 += len(odds) - tmp
        key = r_o[str(tmp)]
        if key in _e.keys():
            _e[key] = 0
        ans1 += len(evens) - max(_e.values())

        ans2 = 0
        _o = collections.Counter(odds)
        r_o = {str(v): k for k, v in _o.items()}
        _e = collections.Counter(evens)
        r_e = {str(v): k for k, v in _e.items()}
        tmp = max(_e.values())
        ans2 += len(evens) - tmp
        key = r_e[str(tmp)]
        if key in _o.keys():
            _o[key] = 0
        ans2 += len(evens) - max(_o.values())

        return str(min(ans1, ans2))


if __name__ == '__main__':
    print(solve("\n".join([input(), input()])))
