from test_demo.deleniye import deleniye
import pytest


@pytest.mark.parametrize('a, b, result', [(10, 2, 5),
                                          (500, 5, 100),
                                          (-10, -5, 2),
                                          (6, 4, 1.5),
                                          ])
def test_deleleniye_good(a, b, result):
    assert deleniye(a, b) == result


@pytest.mark.parametrize('a1, b1, result1', [(10, 0, ZeroDivisionError),
                                             (10, '2', TypeError)
                                             ])
def test_deleleniye_bad(a1, b1, result1):
    with pytest.raises(result1):
        assert deleniye(a1, b1)
