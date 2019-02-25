def solve(string):
    return str(min([abs(753 - int(x + y + z)) for x, y, z in zip(string, string[1:], string[2:])]))


if __name__ == '__main__':
    print(solve(input()))
