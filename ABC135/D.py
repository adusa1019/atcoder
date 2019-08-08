def solve(string):
    n = len(string)
    q_pos = [i for i in range(n) if string[n - i - 1] == "?"]
    table = [[0] * 13 for _ in range(2)]
    table[0][int(string.replace("?", "0")) % 13] = 1
    for i in range(len(q_pos)):
        base = pow(10, q_pos[i], 13)
        for j in range(13):
            for k in range(10):
                table[1][(j + k * base) % 13] += table[0][j]
        for j in range(13):
            table[1][j] %= (10**9 + 7)
        table[0] = table[1]
        table[1] = [0] * 13
    return str(table[0][5])


if __name__ == '__main__':
    print(solve(input()))
