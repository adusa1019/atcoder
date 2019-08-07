def solve(string):
    return str(
        len(string) - max(sum([s == str(i % 2) for i, s in enumerate(string)]),
                          sum([s == str(i % 2) for i, s in enumerate(string, start=1)])))


if __name__ == '__main__':
    print(solve(input()))
