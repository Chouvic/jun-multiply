"""A Multiplication module"""
import numpy as np


class Multiplication:
    """
    Instantiate a multiplication operation
    Numbers will be multiplied by the given multiplier.

    :param multiplier: The multiplier.
    :type  multiplier: int
    """

    def __init__(self, multiplier: int):
        self.multiplier = multiplier

    def multiply(self, number: int) -> int:
        """
        Multiply a given number by the multiplier

        :param number: The number to multiply
        :return:       Result of the multiplication
        """
        # Using NumPy.dot() to multiply the numbers
        return np.dot(number, self.multiplier)
