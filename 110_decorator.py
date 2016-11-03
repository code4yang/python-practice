#!/usr/bin/env python
"""
测试装饰器的使用方法
"""
import functools


def log_before(func_name):
    """
    functools.wraps(func) 加上这个是为了使装饰器修饰的方法名保持原来的名字，否则会变成装饰器内部的名称deco
    :param func_name: 函数名
    :return:
    """

    @functools.wraps(func_name)
    def deco(*arg, **kwargs):
        print("log before")
        return func_name(*arg, **kwargs)

    return deco


def log_after(func_name):
    """
    显示在函数运行后的log
    :param func_name:
    :return:
    """
    @functools.wraps(func_name)
    def after(*args, **kwargs):
        result = func_name(*args, **kwargs)
        print("log after")
        return result

    return after


@log_before
@log_after
def func(a):
    print(func.__name__ + " func running " + str(a))


if __name__ == '__main__':
    func(11)
