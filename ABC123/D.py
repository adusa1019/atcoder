def my_solve(string):
    x, y, z, k, *abc = map(int, string.split())
    a, b, c = abc[:x], abc[x:x + y], abc[x + y:]
    ab = sorted([_a + _b for _b in b for _a in a])[-k:]
    *abc, = map(str, sorted([_ab + _c for _c in c for _ab in ab], reverse=True)[:k])
    return "\n".join(abc)


def solve2(string):
    x, y, z, k, *abc = map(int, string.split())
    a, b, c = map(sorted, [abc[:x], abc[x:x + y], abc[x + y:]])
    ans = []
    for ia in range(1, x + 1):
        for ib in range(1, y + 1):
            for ic in range(1, z + 1):
                if ia * ib * ic <= k:
                    ans.append(a[x - ia] + b[y - ib] + c[z - ic])
                else:
                    break
    return "\n".join(list(map(str, sorted(ans, reverse=True)[:k])))


def solve(string):
    import heapq
    x, y, z, k, *abc = map(int, string.split())
    a, b, c = map(lambda x: sorted(x, reverse=True), [abc[:x], abc[x:x + y], abc[x + y:]])
    hq = []
    heapq.heappush(hq, (-(a[0] + b[0] + c[0]), 0, 0, 0))
    ans = []
    check = set([(0, 0, 0)])
    for _ in range(k):
        m, i, j, k = heapq.heappop(hq)
        ans.append(str(-m))
        if i + 1 < x and (i + 1, j, k) not in check:
            heapq.heappush(hq, (-(a[i + 1] + b[j] + c[k]), i + 1, j, k))
            check.add((i + 1, j, k))
        if j + 1 < y and (i, j + 1, k) not in check:
            heapq.heappush(hq, (-(a[i] + b[j + 1] + c[k]), i, j + 1, k))
            check.add((i, j + 1, k))
        if k + 1 < z and (i, j, k + 1) not in check:
            heapq.heappush(hq, (-(a[i] + b[j] + c[k + 1]), i, j, k + 1))
            check.add((i, j, k + 1))
    return "\n".join(ans)


if __name__ == '__main__':
    print(solve('\n'.join([input() for _ in range(4)])))
