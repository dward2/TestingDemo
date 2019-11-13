import pytest
from datetime import datetime


@pytest.mark.parametrize("a, b, expected", [
                          (2, 3, 5),
                          (3, 7, 10),
                          (-2, 5, 3),
                          (2, 10, 12),
                          (0.1, 0.2, 0.3),
                          ])
def test_add(a, b, expected):
    from calculate import add
    print("a={},b={}".format(a, b))
    result = add(a, b)
    assert result == pytest.approx(expected)


def test_subtract():
    from calculate import subtract
    # timestamp = datetime.now()
    timestamp = datetime(1, 1, 1, 1, 1, 1, 1)
    timestampstr = timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
    # timestampstr1 = timestamp.strftime("%y-%m-%d %H:%M:%S.%f")
    print(timestampstr)
    # print(timestampstr1)
    result = subtract(6, 3)
    assert result == 3


def test_multiply():
    from calculate import multiply
    result = multiply(2, 3)
    assert result == 6
