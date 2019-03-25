def solve(string):
    abc = sorted(map(int, string.split()))
    ans = 0
    oe = sum([_abc % 2 == 0 for _abc in abc])
    if 1 <= oe <= 2:
        for i, _ in enumerate(abc):
            if abc[i] % 2 == oe % 2:
                abc[i] += 1
        ans += 1
    return str(ans + (abc[-1] - abc[0]) // 2 + (abc[-1] - abc[1]) // 2)


if __name__ == '__main__':
    print(solve(input()))
