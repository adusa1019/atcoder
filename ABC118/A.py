#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solve(string):
    a, b = map(int, string.split())
    return str(a + b) if b % a == 0 else str(b - a)


if __name__ == '__main__':
    print(solve(input()))
