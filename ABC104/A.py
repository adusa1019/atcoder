def solve(string):
    r = int(string)
    return "ABC" if r < 1200 else "ARC" if r < 2800 else "AGC"


if __name__ == '__main__':
    print(solve(input()))
