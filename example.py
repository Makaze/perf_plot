from perf_plot import timeit, perf_test
import sys

sys.dont_write_bytecode = 1  # Unclude this in all test files to aviod pycache

d = dict()


@timeit
def key_test(num: int):
    vals = d.values()


def n(*args):
    pass


def make_dict(num: int):
    d = {key: key for key in range(num)}


@timeit
def unpack_test(num: int):
    vals = [*d]


perf_test(
    [
        unpack_test,
        key_test,
    ],
    begin=10**3,
    bound=10**5,
    step=10**3,
    callbacks=[make_dict],
)
