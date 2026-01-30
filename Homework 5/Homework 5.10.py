class SingletonMeta(type):
    """
    Metaclass that implements the Singleton pattern.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Controls the creation of class instances.
        If an instance already exists, returns it.
        Otherwise, creates a new one.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print("Creating instance")


obj1 = Singleton()  # Creating instance
obj2 = Singleton()
print(obj1 is obj2)  # True
