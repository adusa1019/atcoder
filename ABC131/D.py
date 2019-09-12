from operator import itemgetter


def solve(string):
    n, *ab = map(int, string.split())
    ab = sorted(zip(*[iter(ab)] * 2), key=itemgetter(1))
    past = 0
    for a, b in ab:
        past += a
        if past > b:
            return "No"
    return "Yes"


if __name__ == '__main__':
    n = int(input())
    print(solve('{}\n'.format(n) + '\n'.join([input() for _ in range(n)])))
