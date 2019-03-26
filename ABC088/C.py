def solve(string):
    c11, c12, c13, c21, c22, c23, c31, c32, c33 = map(int, string.split())
    check = c11 - c12 == c21 - c22 == c31 - c32 and c12 - c13 == c22 - c23 == c32 - c33 and c13 - c11 == c23 - c21 == c33 - c31 and c11 - c21 == c12 - c22 == c13 - c23 and c21 - c31 == c22 - c32 == c23 - c33 and c31 - c11 == c32 - c12 == c33 - c13
    return "Yes" if check else "No"


if __name__ == '__main__':
    n = 3
    print(solve('\n'.join([input() for _ in range(n)])))
