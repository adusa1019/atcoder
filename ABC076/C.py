def solve(string):
    s, t = string.split()
    s, t = s[::-1], t[::-1]
    for i in range(len(s)):
        for j in range(min(len(t), len(s) - i)):
            if s[i + j] != t[j] and s[i + j] != "?":
                break
            if j == len(t) - 1:
                return (s[:i] + t + s[i + len(t):])[::-1].replace("?", "a")
    return "UNRESTORABLE"


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
