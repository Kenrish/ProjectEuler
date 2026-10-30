#2520 is the smallest number that can be divided from each number 1 to 10. without any remainder.
#What is the smallest number which is evenly divisible by numbers 1 to 20.

from math import lcm
from functools import reduce

print(reduce(lcm, range(2,21)))
