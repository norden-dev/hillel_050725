import inspect
import importlib


def analyze_module(module_name: str) -> None:
    """
    Import a module by name and print all its functions and classes
    along with function signatures.
    """
    module = importlib.import_module(module_name)
    members = inspect.getmembers(module)

    functions = []
    classes = []

    for name, obj in members:
        if inspect.isfunction(obj) or inspect.isbuiltin(obj):
            functions.append((name, obj))
        elif inspect.isclass(obj) and obj.__module__ == module_name:
            classes.append((name, obj))

    print("Functions:")
    for name, func in functions:
        try:
            sig = inspect.signature(func)
            print(f"- {name}{sig}")
        except ValueError:
            print(f"- {name}(...)")

    print("\nClasses:")
    if classes:
        for name, cls in classes:
            print(f"- {name}")
    else:
        print("- <no classes in the module>")


analyze_module("math")
