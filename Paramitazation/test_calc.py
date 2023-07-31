from calc import add, expo, div
import pytest

@pytest.mark.parametrize('x, y, sum',
                        [
                            (7, 3, 10),
                            ('Hello', 'World', 'HelloWorld'),
                            (10.5, 25.5, 36)
                        ]    
                        )
def test_add(x, y, sum):
    assert add(x, y) == sum


@pytest.mark.parametrize('x, y, sqr',
                        [
                            (2, 3, 8),
                            (-2, 2, 4),
                            (1, -2, 1),
                            (-2, -2, 0.25)
                        ]
                        )
def test_sqr(x, y, sqr):
    assert expo(x, y) == sqr

@pytest.mark.parametrize('x, y, prod',
                        [
                            (4, 2, 2),
                            (85558758, 2, 42779379),
                            (-4, 2, -2),
                            (-2, -2, 1),
                            (-2, 0, None)
                        ]
                        )
def test_div(x, y, prod):
    assert div(x, y) == prod