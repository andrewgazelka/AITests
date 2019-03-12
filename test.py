import pytest

from simulated_annealing import distance2


def test_min():
    points = [(0, 0), (0, 300), (300, 300), (300, 0)]
    assert 36_000 == distance2(points)


if __name__ == "__main__":
    pytest.main()
