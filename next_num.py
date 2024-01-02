import functools
import random
from typing import Any


def _get_random() -> float:
    """Return a float value within 0 to 1"""
    return random.random()


class RandomGen(object):
    # TODO: Move initialization of nums and probabilities
    #  as class constructor or method
    # Values that may be returned by next_num()
    _random_nums: list[Any] = [1, 2, 3]
    # Probability of the occurrence of random_nums
    _probabilities: list[float] = [0.1, 0.5, 0.4]

    def next_num(self):
        """
        Returns one of the randomNums. When this method is called multiple
        times over a long period, it should return the numbers roughly with
        the initialized probabilities.
        """
        self._validate()
        sorted_num, sorted_prob = self._sorted_pair()
        random_prob = _get_random()
        pre = 0
        for idx, prob in enumerate(sorted_prob):
            if pre < random_prob <= prob or idx == len(sorted_prob) - 1:
                return sorted_num[idx]
            pre = prob
        # We have validated the inputs so values will be returned

    def _validate(self):
        # Validate inputs to ensure data integrity
        if not self._random_nums or not self._probabilities:
            raise ValueError(
                "Both random numbers and probability should be provided"
            )
        if len(self._random_nums) != len(self._probabilities):
            raise ValueError(
                "Number of random values should match number of probabilities"
            )
        # TODO: Check real requirements, it might not necessarily to be 1
        #  if we define a rule to return an agreed value (e.g. None) if sum
        #  is not 1
        if sum(self._probabilities) != 1:
            raise ValueError(
                "Sum of all probability should equal to 1"
            )
        if any(p < 0 for p in self._probabilities):
            raise ValueError('Any probability should be positive')

    @functools.cache
    def _sorted_pair(self) -> tuple[list[Any], list[float]]:
        """Return a group of pair that sorted by probabilities"""
        mapping = {}
        for num, prob in zip(self._random_nums, self._probabilities):
            mapping[prob] = num
        sorted_prob = sorted(self._probabilities)
        sorted_num = []
        for prob in sorted_prob:
            sorted_num.append(mapping[prob])
        return sorted_num, sorted_prob


if __name__ == '__main__':
    r = RandomGen()
    print(r.next_num())
