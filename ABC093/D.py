from math import sqrt


def solve(string):
    q, *ab = map(int, string.split())
    ans = []
    for a, b in zip(ab[::2], ab[1::2]):
        c = a * b
        d = int(sqrt(c))
        answer = 2 * d - 2
        if d * d == c:
            answer -= 1
        if d * (d + 1) < c:
            answer += 1
        if a == b:
            answer += 1
        ans.append(str(answer))
    return "\n".join(ans)


if __name__ == '__main__':
    n = int(input())
    print(solve('{}\n'.format(n) + '\n'.join([input() for _ in range(n)])))
