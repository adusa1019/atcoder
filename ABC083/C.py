def solve(string):
    x, y = map(int, string.split())
    ans = 0
    while x <= y:
        x *= 2
        ans += 1
    return str(ans)


if __name__ == '__main__':
    print(solve(input()))
