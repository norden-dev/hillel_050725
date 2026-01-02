import builtins


def sum(*args: list, **kwargs: list) -> str:
    """Shadow the built-in sum function"""
    return "This is my custom sum function!"


numbers = [1, 2, 3]
print(sum(numbers))
print(builtins.sum(numbers))
