def solve(string):
    ins = list(map(int, string.split("\n")))[1:]
    ins.sort()
    ins[-1] //= 2
    return str(sum(ins))


if __name__ == '__main__':
    n = int(input())
    ins = [input() for _ in range(n)]
    print(solve("{}\n{}".format(n, "\n".join(ins))))
