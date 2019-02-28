def solve(string):
    n, m = map(int, string.split())
    d = [i for i in range(1, int(m**0.5) + 1) if m % i == 0]
    d.extend([m // i for i in d])
    return str(max([i for i in d if m // i >= n]))


if __name__ == '__main__':
    print(solve(input()))
