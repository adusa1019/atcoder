def solve(string):
    n, k, s = string.split()
    c = s.count("RL") + s.count("LR")
    return str(int(n) - max(1, c + 1 - 2 * int(k)))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
