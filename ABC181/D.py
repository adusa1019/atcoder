from collections import Counter


def solve(string):
    if len(string) <= 2:
        return "Yes" if int(string) % 8 == 0 or int(string[::-1]) % 8 == 0 else "No"
    s = Counter(string)
    for i in range(112, 1000, 8):
        if not Counter(str(i)) - s:
            return ("Yes")
    return "No"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
