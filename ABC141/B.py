def solve(string):
    s = string
    return "No" if "L" in s[::2] or "R" in s[1::2] else "Yes"


if __name__ == '__main__':
    print(solve(input()))
