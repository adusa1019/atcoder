def solve(string):
    n, *b = map(int, string.split())
    b.append(b[-1])
    return str(b[0] + sum([min(b0, b1) for b0, b1 in zip(b, b[1:])]))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
