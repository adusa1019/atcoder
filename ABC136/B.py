def solve(string):
    base = int(string) if len(string) % 2 == 1 else 10**(len(string) - 1) - 1
    excepts = sum([9 * 10**(i - 1) for i in range(2, len(string), 2)])
    return str(base - excepts)


if __name__ == '__main__':
    print(solve(input()))
