# fibonacci series using lambda

from functools import reduce

fib_numbers = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

print("Fibonacci Series:",fib_numbers(10))
