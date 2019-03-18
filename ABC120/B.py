def solve(string):
    a, b, k = map(int, string.split())
    for i in range(min(a, b), 0, -1):
        if a % i == b % i == 0:
            k -= 1
        if k == 0:
            return str(i)


if __name__ == '__main__':
    print(solve(input()))
