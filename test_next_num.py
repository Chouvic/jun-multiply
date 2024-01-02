import pytest

from next_num import RandomGen


def test_random_gen_valid_single_value():
    r = RandomGen()
    r._random_nums = [1]
    r._probabilities = [1]
    assert r.next_num() == 1


def test_init_random_gen_negative_prob():
    r = RandomGen()
    r._random_nums = [1, 2]
    r._probabilities = [-1, 2]
    with pytest.raises(ValueError, match="Any probability should be positive"):
        assert r.next_num()


def test_init_random_gen_mismatch():
    r = RandomGen()
    r._random_nums = [1]
    r._probabilities = [0.5, 0.5]
    with pytest.raises(ValueError, match="Number of random values should match number of probabilities"):
        assert r.next_num()


