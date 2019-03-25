def solve(string):
    return "Yes" if string.find("a") >= 0 and string.find("b") >= 0 and string.find(
        "c") >= 0 else "No"


if __name__ == '__main__':
    print(solve(input()))
