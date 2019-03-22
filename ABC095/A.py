def solve(string):
    return str(700 + 100*string.count("o"))


if __name__ == '__main__':
    print(solve(input()))
