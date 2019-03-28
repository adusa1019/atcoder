import pytest
from B import solve


def test_solve():
    assert solve('yx\naxy') == 'Yes'
    assert solve('ratcode\natlas') == 'Yes'
    assert solve('cd\nabc') == 'No'
    assert solve('w\nww') == 'Yes'
    assert solve('zzz\nzzz') == 'No'
