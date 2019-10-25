def solve(string):
    n, *l = map(int, string.split())
    l.sort(reverse=True)
    nums = 0
    for i, a in enumerate(l[:-2]):
        j, k = i + 1, n - 1
        while (j < k):
            if (a < l[j] + l[k]):
                nums += k - j
                j += 1
            else:
                k -= 1
    return str(nums)


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
