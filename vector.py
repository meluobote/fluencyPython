# -*- coding: utf-8 -*-
"""
   File Name：     vector
   Description :
   Author :       meluobote
   date：          2018/11/5
"""
import math

class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        return (it for it in (self.x, self.y))

    # def __next__(self):
    #     return (it for it in (self.x, self.y))
    def __repr__(self):
        return f'repr: {type(self).__name__}'

    def __str__(self):
        return f'str: {type(self).__name__}'

    def __bytes__(self):
        return bytes(str(self), encoding='utf-8')

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(self)

    @classmethod
    def frombytes

if __name__ == '__main__':
    v = Vector2d(1, 2)
    print(tuple(v))
    print(list(v))
