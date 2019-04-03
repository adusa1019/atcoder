def solve(string):
    x, y = string.split()
    return "=" if x == y else "<" if x < y else ">"


if __name__ == '__main__':
    print(solve(input()))
