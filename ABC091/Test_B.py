import pytest
from B import solve


def test_solve():
    assert solve('3\napple\norange\napple\n1\ngrape') == '2'
    assert solve('3\napple\norange\napple\n5\napple\napple\napple\napple\napple') == '1'
    assert solve('1\nvoldemort\n10\nvoldemort\nvoldemort\nvoldemort\nvoldemort\nvoldemort\nvoldemort\nvoldemort\nvoldemort\nvoldemort\nvoldemort') == '0'
    assert solve('6\nred\nred\nblue\nyellow\nyellow\nred\n5\nred\nred\nyellow\ngreen\nblue') == '1'
