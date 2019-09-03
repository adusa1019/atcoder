def solve(string):
    n, *h = map(int, string.split())
    s = "".join(["1" if h0 >= h1 else "0" for h0, h1 in zip(h, h[1:])]).split("0")
    return str(max(list(map(len, s))))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
