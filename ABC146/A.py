def solve(string):
    l = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    return str(7 - l.index(string))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
