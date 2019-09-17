import pytest
from B import solve


def test_solve():
    assert solve('RUDLUDR') == 'Yes'
    assert solve('DULL') == 'No'
    assert solve('UUUUUUUUUUUUUUU') == 'Yes'
    assert solve('ULURU') == 'No'
    assert solve('RDULULDURURLRDULRLR') == 'Yes'
