def solve(string):
    ans = 0
    i = 0
    while i < len(string):
        j = 0
        while i + j < len(string) and string[i + j] in "ATGC":
            j += 1
        ans = max(ans, j)
        i += j + 1
    return str(ans)


if __name__ == '__main__':
    print(solve(input()))
