
from geom import point, getx, gety


def test_creation_point():
    p = point(22,7)
    assert 22 ==getx(p)
    assert 7 == gety(p)
