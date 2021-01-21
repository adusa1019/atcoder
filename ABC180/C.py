def solve(string):
    n = int(string)
    ans = []
    for i in range(1, int(n**0.5)+1):
        if n // i == n / i:
            ans.append(i)
            ans.append(n // i)
    if int(n**0.5) == n**0.5:
        ans.pop()
    return "\n".join(map(str, sorted(ans)))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
