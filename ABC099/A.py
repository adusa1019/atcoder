def solve(string):
    return "ABC" if int(string) < 1000 else "ABD"


if __name__ == '__main__':
    print(solve(input()))
