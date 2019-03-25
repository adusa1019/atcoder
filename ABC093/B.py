def solve(string):
    a, b, k = map(int, string.split())
    l = set(range(a, min(a + k, b)))
    r = set(range(max(a, b - k + 1), b + 1))
    return "\n".join(map(str, sorted(l | r)))


if __name__ == '__main__':
    print(solve(input()))
