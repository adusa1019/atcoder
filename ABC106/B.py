def solve(string):
    n = int(string)
    return "0" if n < 105 else "1" if n < 135 else "2" if n < 165 else "3" if n < 189 else "4" if n < 195 else "5"


if __name__ == '__main__':
    print(solve(input()))
