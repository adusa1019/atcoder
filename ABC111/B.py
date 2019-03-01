def solve(string):
    if int(string[0]) == int(string[1]) == int(string[2]):
        return string
    elif int(string[0] * 3) > int(string):
        return string[0] * 3
    else:
        return str(int(string[0]) + 1) * 3


if __name__ == '__main__':
    print(solve(input()))
