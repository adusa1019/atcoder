def solve(string):
    k, x = map(int, string.split())
    return " ".join([str(i) for i in range(x - k + 1, x + k)])


if __name__ == '__main__':
    print(solve(input()))
