import mem
import timeit
import sys


def mylist(length):
    sum_mylist = sum([i**2 for i in range(length)])
    print(sum_mylist)


def mygen(length):
    # for i in range(length):
    #     yield i**2
    sum_mygen = sum((i**2 for i in range(length)))
    print(sum_mygen)
    return 


def test_methods(method):
    print(method.__name__)
    print(f"Memory Before: {mem.memory_usage_resource()}Mb")
    t1 = timeit.default_timer()
    a = method(20000000)
    t2 = timeit.default_timer()
    print(f"{method.__name__} took {t2 - t1} seconds")
    print(f"Peak Memory Usage: {mem.memory_usage_resource()}Mb" + "\n")


test_methods(eval(sys.argv[1]))
