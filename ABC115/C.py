def solve(string):
    n, k = map(int, string.split("\n")[0].split(" "))
    ins = list(map(int, string.split("\n")[1:]))
    ins.sort()
    return str(min([ins[i + k - 1] - ins[i] for i in range(len(ins) - k + 1)]))


if __name__ == '__main__':
    n, k = map(int, input().split(" "))
    ins = [input() for _ in range(n)]
    print(solve("{} {}\n{}".format(n, k, "\n".join(ins))))
