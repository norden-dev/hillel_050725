from typing import Dict, Callable, Type, Any


def say_hello(self) -> str:
    return "Hello!"


def say_goodbye(self) -> str:
    return "Goodbye!"


methods: Dict[str, Callable[..., Any]] = {
    "say_hello": say_hello,
    "say_goodbye": say_goodbye
}


def create_class(class_name: str, methods: Dict[str, Callable[..., Any]]) -> Type[Any]:
    """
    Dynamically create a class with the given name and methods.

    """
    return type(class_name, (object,), methods)


MyDynamicClass = create_class("MyDynamicClass", methods)

obj = MyDynamicClass()
print(obj.say_hello())
print(obj.say_goodbye())
