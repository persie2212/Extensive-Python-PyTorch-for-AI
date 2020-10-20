import random
import math
import decimal
from decimal import Decimal

class Qualean():
    def __init__(self, x):
        self.x = x
        with decimal.localcontext() as ctx:
            ctx.rounding = decimal.ROUND_HALF_UP
            ctx.prec = 10
            self.y = self.x * Decimal(random.uniform(-1, 1))

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if x == 1 or x == 0 or x == -1:
            self._x = x
        else:
            raise ValueError("Value must be 0 or 1 or -1")

    def __str__(self):
        return 'Value: {0}'.format(self.y)

    def __repr__(self):
        return 'Value: {0}'.format(self.y)

    def __add__(self, value):
        return self.y + value.y

    def __eq__(self, value):
        return self.y == value.y

    def __float__(self):
        return float(self.y)

    def __ge__(self, value):
        return self.y >= value.y

    def __gt__(self, value):
        return self.y > value.y

    def __le__(self, value):
        return self.y <= value.y

    def __lt__(self, value):
        return self.y < value.y

    def __mul__(self, value):
        return self.y * value

    def __invertsign__(self):
        return -self.y

    def __sqrt__(self):
        if self.y >= 0:
            return math.sqrt(self.y)
        else:
            return 'Value: {0}i'.format(math.sqrt(-self.y))

    def __and__(self, value):
        if self.y and value.y:
            return True
        else:
            return False

    def __or__(self, value):
        if self.y or value.y:
            return False
        else:
            return True

    def __bool__(self):
        return self.y != 0