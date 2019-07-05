def solve(string):
    for _s in string:
        if string.count(_s) != 2:
            return "No"
    return "Yes"


if __name__ == '__main__':
    print(solve(input()))
