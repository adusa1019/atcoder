def solve(string):
    a, b = map(int, string.split())
    count = 0
    for i in range(a, b + 1):
        if str(i) == str(i)[::-1]:
            count += 1
    return str(count)


if __name__ == '__main__':
    print(solve(input()))
