from typing import Callable


def memoize(func: Callable) -> Callable:
    """Decorator for caching function results."""
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def factorial(n: int) -> int:
    print(f" факториал {n}")
    if n < 2:
        return 1
    return n * factorial(n - 1)


@memoize
def fibonacci(n: int) -> int:
    print(f"фібоначи fib({n})")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(f"Факториал 5: {factorial(5)}")
print(f"Факториал 3: {factorial(3)}")
print(f"fib(10): {fibonacci(10)}")