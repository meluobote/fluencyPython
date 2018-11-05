# -*- coding: utf-8 -*-
'''
@File  : doubleDimensionCalculate.py
@Author: Piepis
@Date  : 2018/10/16 9:04
@Desc  : 
'''
import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        #有下面两个方法
        # return math.sqrt(math.pow(3, 2) + math.pow(4, 2))
        return math.hypot(self.x, self.y)
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    # x和y同时乘以一个数
    def __mul__(self, scatter):
        return Vector(self.x * scatter, self.y * scatter)


if __name__ == '__main__':
    v1 = Vector(3, 4)
    v2 = Vector(5, 12)
    print(v1 + v2)
    print(v1 * 3)
