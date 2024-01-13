import numpy as np
def func(x, L, x0):
    return L / (1 + np.exp(-(x - x0)))


def func2(x, a, b):
    return a * b ** x


def display_func(L, x0):
    return fr"$y = \frac{{{round(L, 1)}}}{{1+e^{{-(x-{round(x0, 3)})}}}}$"


def display_func2(a, b):
    return fr"$y = {round(a, 3)}\times {round(b, 3)}^{{x}}$"