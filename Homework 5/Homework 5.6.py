from typing import Any


class Proxy:
    """
    A proxy class that intercepts method calls to another object
    and logs the method name and arguments before forwarding the call.
    """

    def __init__(self, obj: Any) -> None:
        self._obj = obj

    def __getattr__(self, name: str) -> Any:
        attr = getattr(self._obj, name)

        if callable(attr):
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                print(f"Calling method: {name} with args: {args}")
                if kwargs:
                    print(f"Kwargs: {kwargs}")
                return attr(*args, **kwargs)

            return wrapper

        return attr


class MyClass:
    def greet(self, name):
        return f"Hello, {name}!"


obj = MyClass()
proxy = Proxy(obj)

print(proxy.greet("Alice"))
