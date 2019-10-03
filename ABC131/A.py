def solve(string):
    return "Bad" if any([s1 == s2 for s1, s2 in zip(string, string[1:])]) else "Good"


if __name__ == '__main__':
    print(solve(input()))
