import pytest
from D import solve


def test_solve():
    assert solve('??2??5') == '768'
    assert solve('?44') == '1'
    assert solve('7?4') == '0'
    assert solve('?6?42???8??2??06243????9??3???7258??5??7???????774????4?1??17???9?5?70???76???') == '153716888'