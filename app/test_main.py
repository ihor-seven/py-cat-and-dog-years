from app.main import get_human_age


def test_should_return_zero_for_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_for_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_should_increase_after_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_should_increase_after_third_threshold() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_values_should_be_calculated_correctly() -> None:
    assert get_human_age(100, 100) == [21, 17]
