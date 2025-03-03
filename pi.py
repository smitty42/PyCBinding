import time
from threading import Thread
from ctypes import CDLL

import termplotlib as tpl
import numpy as np
import timeit

so_file = "./pi.so"
c_pi = CDLL(so_file)


def taylor_pi_list(k=100):
    pi = []
    n = 1
    while n < k:
        pi += [((-1) ** (n + 1)) * (4 / (2**n - 1))]
        n += 1

    return pi


def taylor_pi_inf(pi=np.longdouble(0.0)):
    n = 1
    while True:
        pi += ((-1) ** (n + 1)) / ((2 * n - 1))
        n += 1
        # print(f"Python: {4 * pi}", end="", flush=True)
        print(f"Python: {4 * pi}")


def taylor_pi(pi=np.longdouble(0.0), k=10000000):
    n = 1
    while n < k:
        pi += ((-1) ** (n + 1)) / ((2 * n - 1))
        n += 1
        # print(4 * pi)

    return 4 * pi


def plot():
    x = np.linspace(0, 10, 10)
    y = taylor_pi_list(k=10)
    fig = tpl.figure()
    fig.plot(x, y, width=60, height=20)
    fig.show()


py_pi = Thread(target=taylor_pi_inf)
py_pi.start()

c_pi = Thread(target=c_pi.taylor_pi())
c_pi.start()


# print(timeit.timeit("taylor_pi()", setup="from __main__ import taylor_pi", number=1))
