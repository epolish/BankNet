from math import sqrt
from functools import reduce

class Mahalanobis:
    def distance(self, vector):
        return sqrt(reduce((lambda x, y: x+y), map(lambda x: x**2, vector)))