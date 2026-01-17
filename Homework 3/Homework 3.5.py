class Mymethod:

    def __init__(self, data: list) -> None:
        """A custom collection class that implements its own versions
        of len(), sum(), and min() functions, and supports iteration
        and indexing."""
        self.data = data

    def __len__(self) -> int:
        """ Initializes the collection with a list of integers."""
        return len(self.data)

    def __iter__(self) -> iter:
        """Returns an iterator over the elements in the collection."""
        return iter(self.data)

    def __getitem__(self, item: int) -> int:
        """Returns the element at the specified index."""
        return self.data[item]

    def my_len(self) -> int:
        """Custom implementation of len()."""
        counter = 0
        for _ in self.data:
            counter += 1
        return counter

    def my_sum(self) -> int:
        """Custom implementation of sum()."""
        total = 0
        for element in self.data:
            total += element
        return total

    def my_min(self) -> int:
        """Custom implementation of min()."""
        min_element = self.data[0]
        for element in self.data:
            if element < min_element:
                min_element = element
        return min_element


my_lst = Mymethod([0, 1, 2, -1])
print(my_lst.my_min())
print(my_lst.my_len())
print(my_lst.my_sum())
