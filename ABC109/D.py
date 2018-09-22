def solve(string):
    ins = string.split("\n")
    h, w = map(int, ins[0].split(" "))
    a = [list(map(lambda x: int(x) % 2 == 1, _i.strip().split(" "))) for _i in ins[1:]]
    move = []
    for i in range(h):
        for j in range(w):
            if not a[i][j]:
                continue
            if j < w - 1:
                a[i][j + 1] ^= True
                move.append("{} {} {} {}".format(i + 1, j + 1, i + 1, j + 2))
            elif i < h - 1:
                a[i + 1][j] ^= True
                move.append("{} {} {} {}".format(i + 1, j + 1, i + 2, j + 1))
    move.insert(0, str(len(move)))
    return "\n".join(move)


if __name__ == '__main__':
    line = input().strip()
    h, w = map(int, line.split(" "))
    ins = [input() for _ in range(h)]
    ins.insert(0, line)
    print(solve("\n".join(ins)))
