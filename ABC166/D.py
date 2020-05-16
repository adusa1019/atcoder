def solve(string):
    x = int(string)
    a = {i**5: i for i in range(-200, 200)}
    for i in range(-200, 200):
        if x + i ** 5 in a:
            return str(f"{a[x+i**5]} {i}")


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
