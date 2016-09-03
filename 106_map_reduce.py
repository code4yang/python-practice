"""
map 里的第一个参数接受一个函数，第二个参数接受一个Iterable，返回一个Iterable。 第一个函数只能有一个参数
reduce 里第一个参数接受一个函数，这个函数必须有两个参数。reduce将结果和序列的下一个元素进行累积计算。
"""
from functools import reduce


def func_a(x, y):
    return x * 10 + y


def func_b(x):
    return x*x


if __name__ == '__main__':
    a = reduce(func_a, [1, 2, 3, 4, 5])
    b = map(func_b, [1, 2, 3, 4, 5])
    print(a)
    print(list(b))
