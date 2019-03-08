def solve(string):
    n, k = map(int, string.split())
    return "0" if n % k == 0 else "1"


if __name__ == '__main__':
    print(solve(input()))
