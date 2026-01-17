from typing import List


class Person:
    """ Represent a person with a name and age."""

    def __init__(self, name: str, age: int) -> None:
        """Initialize a Person instance with name and age."""
        self.name = name
        self.age = age

    def __lt__(self, other: 'Person') -> bool:
        """ Compare if the current Person instance is younger than another Person."""
        return self.age < other.age

    def __eq__(self, other: 'Person') -> bool:
        """Compare equality between two Person instances based on age."""
        return self.age == other.age

    def __gt__(self, other: 'Person') -> bool:
        """Compare if the current Person instance is older than another Person."""
        return self.age > other.age

    def __repr__(self) -> str:
        return f"Person name: {self.name} Age: {self.age}"

    @staticmethod
    def sort_people_by_age(people: List['Person']) -> List['Person']:
        """Sorts a list of people by age."""
        return sorted(people)


p1 = Person("Igor", 40)
p2 = Person("Maria", 35)
p3 = Person("Dima", 33)
people = [p1, p2, p3]

sorted_people = Person.sort_people_by_age(people)
print("Sorted list:")
for person in sorted_people:
    print(person)
