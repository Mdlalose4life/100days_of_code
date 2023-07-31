from parameterize import parameterized

@parameterized([
    (1, 1, 2)
])
def test_add(a, b, sum):
    assert_equal(a + b, sum)