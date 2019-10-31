def solve(string):
    n = int(string)
    m = set([i * j for i in range(1, 10) for j in range(1, 10)])
    return "Yes" if n in m else "No"


if __name__ == '__main__':
    print(solve(input()))
