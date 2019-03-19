import pytest
from C import solve


def test_solve():
    assert solve('aba\n4') == 'b'
    assert solve('atcoderandatcodeer\n5') == 'andat'
    assert solve('z\n1') == 'z'
    assert solve('cba\n1') == 'a'
    assert solve('cba\n2') == 'b'
    assert solve('cba\n3') == 'ba'
    assert solve('cba\n4') == 'c'
    assert solve('cba\n5') == 'cb'
    hoge = "a" * 5000
    assert solve('{}\n3'.format(hoge)) == 'aaa'
