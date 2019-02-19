#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# after python 3.5
# from math import gcd
# before or equal python 3.4
from fractions import gcd
from functools import reduce


def solve(string):
    n, *a = map(int, string.split())
    return str(reduce(gcd, a))


if __name__ == '__main__':
    print(solve("\n".join([input(), input()])))
