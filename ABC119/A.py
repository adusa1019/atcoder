def solve(string):
    return "Heisei" if string <= "2019/04/30" else "TBD"


if __name__ == '__main__':
    print(solve(input()))
