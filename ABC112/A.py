def solve(string):
    flag, *ab = map(int, string.split())
    return str(sum(ab)) if flag - 1 else "Hello World"


if __name__ == '__main__':
    flag = int(input())
    if flag - 1:
        flag = "{}\n".format(flag) + "\n".join([input(), input()])
    print(solve(str(flag)))
