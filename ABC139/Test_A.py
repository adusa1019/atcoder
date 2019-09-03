import pytest
from A import solve


def test_solve():
    assert solve('CSS\nCSR') == '2'
    assert solve('SSR\nSSR') == '3'
    assert solve('RRR\nSSS') == '0'
