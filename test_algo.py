
import algo

def test_min():
    values = (2, 3, 1, 4, 6)

    val = algo.min(values)
    assert val == 1

def test_max():
    values = (2, 3, 1, 4, 6)

    val = algo.max(values)
    assert val == 6

def test_fib():
    assert fib(0) == 0
    assert fib(1) == 10
    assert fib(10) == 55
