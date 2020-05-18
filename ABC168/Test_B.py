import pytest
from B import solve


def test_solve():
    assert solve('7\nnikoandsolstice') == 'nikoand...'
    assert solve('40\nferelibenterhominesidquodvoluntcredunt') == 'ferelibenterhominesidquodvoluntcredunt'
