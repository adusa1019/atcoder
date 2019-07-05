def solve(string):
    *abcde, = map(int, string.split())
    abcde.sort(key=lambda x: (x-1) % 10)
    return "{}".format(abcde[0] + sum([((i - 1) // 10 + 1) * 10 for i in abcde[1:]]))


if __name__ == '__main__':
    print(solve('\n'.join([input() for _ in range(5)])))
