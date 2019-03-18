from collections import Counter


def solve(string):
    count = Counter(string)
    return str(min(count.values()) * 2) if len(count.keys()) > 1 else "0"


if __name__ == '__main__':
    print(solve(input()))
