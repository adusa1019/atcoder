#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solve(string):
    a, b = map(int, string.split(" "))
    if a * b % 2 != 0:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    print(solve(input()))
