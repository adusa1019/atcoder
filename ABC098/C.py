def solve(string):
    n, s = string.split()
    num_e = s.count("E")
    count_e = count_w = 0
    ans = int(n)
    for _s in s:
        tmp = count_w
        if _s == "E":
            count_e += 1
        else:
            count_w += 1
        tmp += num_e - count_e
        ans = min(ans, tmp)
    return str(ans)


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
