def solve(string):
    n = len(string)
    ans = [0] * n
    count = 0
    for i, a in enumerate(string):
        if a == "R":
            count += 1
            continue
        if count > 0:
            ans[i] += count // 2
            ans[i - 1] += (count + 1) // 2
            count = 0
    for i, a in enumerate(string[::-1]):
        if a == "L":
            count += 1
            continue
        if count > 0:
            ans[n - i - 1] += count // 2
            ans[n - i] += (count + 1) // 2
            count = 0
    return " ".join([str(a) for a in ans])


if __name__ == '__main__':
    print(solve(input()))
