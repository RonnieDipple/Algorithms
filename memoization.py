# This decorator takes a function and returns a wrapped version of the same
# function that implements the caching logic (memoized_func).
#
# I’m using a Python dictionary as a cache here. In Python, using a key to look-up a value in a dictionary is quick.
# This makes dict a good choice as the data structure for the function result cache.
#
# Whenever the decorated function gets called, we check if the parameters are already in the cache. If they are,
# then the cached result is returned. So, instead of re-computing the result, we quickly return it from the cache.
#
# If the result isn’t in the cache, we must update the cache so we can save some time in the future. Therefore,
# we first compute the missing result, store it in the cache, and then return it to the caller.
#
# Bam, memoization!


def memoized(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func



# Calculating the n-th Fibonacci number this way has O(2^n) time complexity—it takes exponential time to complete.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


