def solve(string):
    N, M, X, Y, *xy = map(int, string.split())
    x, y = xy[:N], xy[N:]
    max_x = max(x)
    min_y = min(y)
    if min_y <= max_x or min_y <= X or Y <= max_x:
        return "War"
    else:
        return "No War"


if __name__ == '__main__':
    print(solve("\n".join([input(), input(), input()])))
