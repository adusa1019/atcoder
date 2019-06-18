def solve(string):
    r, d, x = map(int, string.split())
    ans = []
    for _ in range(10):
        x = r * x - d
        ans.append(str(x))
    return "\n".join(ans)


if __name__ == '__main__':
    print(solve(input()))
