def solve(string):
    *abc, k = map(int, string.split())
    abc = sorted(abc)
    for i in range(k):
        abc[-1] *= 2
    return str(sum(abc))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
