def solve(string):
    ans = 0
    for s in string:
        if s == "+":
            ans += 1
        else:
            ans -= 1
    return str(ans)


if __name__ == '__main__':
    print(solve(input()))
