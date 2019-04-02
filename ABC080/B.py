def solve(string):
    return "Yes" if int(string) % sum(map(int, string)) == 0 else "No"


if __name__ == '__main__':
    print(solve(input()))
