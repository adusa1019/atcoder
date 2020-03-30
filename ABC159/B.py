def solve(string):
    n = len(string)
    pre, post = string[:(n - 1) // 2], string[(n + 3) // 2 - 1:]
    return "Yes" if string == string[::-1] and pre == pre[::-1] and post == post[::-1] else "No"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
