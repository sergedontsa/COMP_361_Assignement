# Simpson's Rule
import numpy as np
import matplotlib.pyplot as plt


def midpoint(f, a, b, n):
    """
    :param f: function vectorized of a single variable
    :param a: number
    :param b:  number
    :param n: integer
    :return:
    """
    h = float((b - a) / n)
    result = 0
    for i in range(n):
        result += f((a + h / 2) + i * h)
    result *= h
    return result


def simpson_rule(f, a, b, N=50):
    """
    :param f: function vectorized of a single variable
    :param a:  numbers
    :param b:  numbers
    :param N: (even) integer Number of sub-interval of [a, b]
    :return: float an approximation of the integral of f(x) from a to b using
             Simpson's rule with N sub-interval of equal length
    """
    dx = (b - a) / N
    x = np.linspace(a, b, N + 1)
    y = f(x)
    s = (dx / 3) * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])
    return s


print(simpson_rule(lambda x: 3 * x ** 2, 0, 1, 10))
