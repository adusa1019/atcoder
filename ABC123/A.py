def solve(string):
    a, *_, e, k = map(int, string.split())
    return "Yay!" if e - a <= k else ":("


if __name__ == '__main__':
    print(solve('\n'.join([input() for _ in range(6)])))
