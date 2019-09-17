def solve(string):
    s = string
    c, l = "SCR", ["Sunny", "Cloudy", "Rainy"]
    return l[(c.index(s[0]) + 1) % 3]


if __name__ == '__main__':
    print(solve(input()))
