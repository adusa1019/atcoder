def solve(string):
    n = int(string)
    base = [(-2)**i for i in range(40)]
    ans = ""
    for b in base:
        if n % abs(2 * b) >= abs(b):
            n -= b
            ans += "1"
        else:
            ans += "0"
        if n == 0:
            break
    return ans[::-1]


if __name__ == '__main__':
    print(solve(input()))
