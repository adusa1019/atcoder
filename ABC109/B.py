def solve(string):
    ins = string.split("\n")
    if len(set(ins[1:])) < int(ins[0]):
        return "No"
    for _p, _n in zip(ins[1:], ins[2:]):
        if _p[-1] != _n[0]:
            return "No"
    return "Yes"


if __name__ == '__main__':
    n = int(input())
    tmp = [str(n)]
    for _ in range(n):
        tmp.append(input())
    print(solve("\n".join(tmp)))
