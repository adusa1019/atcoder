#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solve(string):
    string = string.split("\n")
    n, m = map(int, string[0].split())
    ans = {i + 1 for i in range(m)}
    for loves in string[1:]:
        ans &= set(map(int, loves.split()[1:]))
    return str(len(ans))


if __name__ == '__main__':
    base = input()
    n, m = map(int, base.split())
    tmp = [base]
    for _ in range(n):
        tmp.append(input())
    print(solve('\n'.join(tmp)))
