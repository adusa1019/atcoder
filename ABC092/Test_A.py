import pytest
from A import solve


def test_solve():
    assert solve('600\n300\n220\n420') == '520'
    assert solve('555\n555\n400\n200') == '755'
    assert solve('549\n817\n715\n603') == '1152'
