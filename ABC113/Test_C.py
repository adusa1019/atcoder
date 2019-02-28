import pytest
from C import solve


def test_solve():
    assert solve('2 3\n1 32\n2 63\n1 12') == '000001000002\n000002000001\n000001000001'
    assert solve('2 3\n2 55\n2 77\n2 99') == '000002000001\n000002000002\n000002000003'


def test_run_time():
    ins = "2 100000\n" + "\n".join(["2 {}".format(10**5 - i) for i in range(10**5)])
    outs = "\n".join(["{:06}{:06}".format(2, 10**5 - i) for i in range(10**5)])
    assert solve(ins) == outs
