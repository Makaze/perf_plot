from functools import wraps
import numpy as np
import gnuplotlib as gp
import time

import sys

sys.dont_write_bytecode = 1  # Include this all test files to aviod pycache

timers = dict()


def timeit(func):
    """@timeit decorator: Time a function"""

    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        if func.__name__ not in timers:
            timers[func.__name__] = []
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        timers[func.__name__].append(total_time)
        # first item in the args, ie `args[0]` is `self`
        # print(f"Function {func.__name__} Took {total_time:.4f} seconds")
        return result

    return timeit_wrapper


def perf_test(funcs: list, begin=1, bound=10000, step=100, callbacks=[]):
    """Run a list of functions with a range of inputs, time them, and plot
    their performance

    :param list funcs: A list of tester functions that each take an int and do
    some comparable operations that scale accordingly
    e.g [labmda x: [i for i in range(x)], lamba y: (i for i in range(y))]
    :param int begin: The lower bound of the test, defaults to 1
    :param int bound: The upper bound of the test, defaults to 10000
    :param int step: How much to increment for each iteration, defaults to 100
    :param list callbacks: A list of callbacks to run before testing each
    function, defaults to []
    """
    for f in funcs:
        for i in range(begin, bound + 1, step):
            [c(i) for c in callbacks]
            f(i)
    gp.plot(
        *[
            (
                np.arange(begin, bound + 1, step),
                np.array(timers[f.__name__]),
                {"legend": f.__name__.replace("_", r"\\\_")},
            )
            for f in funcs
        ]
    )
