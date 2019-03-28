from collections import Counter


def solve(string):
    n, *a = map(int, string.split())
    count = Counter(a)
    return str(sum([v if int(k) > v else v - int(k) for k, v in count.items()]))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
