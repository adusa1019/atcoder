import pytest
from D import solve


def test_solve():
    assert solve('2 2 4') == '45.0'
    assert solve('12 21 10') == '89.7834636934'
    assert solve('3 1 8') == '4.2363947991'
