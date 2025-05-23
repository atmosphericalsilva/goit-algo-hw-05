# importing functions
from typing import Callable
import re


def generator_numbers(text):
    # looking for numbers in string
    nums = re.findall(r'(?<=\s)\d+(?=\s)', text)
    n = 0
    # generating numbers
    while n < len(nums):
        yield float(nums[n])
        n += 1


def sum_profit(text: str, gen_func: Callable[[str], list]):
    # summing up numbers in string
    return sum(gen_func(text)) 