def solve(string):
    n, *a_e = map(int, string.split())
    return str(5 + (n + min(a_e) - 1) // min(a_e) - 1)


if __name__ == '__main__':
    print(solve('\n'.join([input() for _ in range(6)])))
