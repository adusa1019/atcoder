def solve(string):
    return "Yes" if string[1] == string[2] and (string[1] == string[0] or
                                                string[1] == string[-1]) else "No"


if __name__ == '__main__':
    print(solve(input()))
