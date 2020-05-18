def solve(string):
    if string[-1] == "3":
        return "bon"
    if string[-1] in ["0", "1", "6", "8"]:
        return "pon"
    return "hon"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
