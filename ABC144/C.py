def solve(string):
    n = int(string)
    for i in range(int(n**0.5), 0, -1):
        if not n % i:
            return str(i + n // i - 2)


if __name__ == '__main__':
    print(solve(input()))
