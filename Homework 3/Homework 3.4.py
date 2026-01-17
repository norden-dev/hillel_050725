class BinaryNumber:
    """
    A class that represents a binary number and allows
    bitwise operations to be performed on it.
    """

    def __init__(self, binary):
        """
        Initializes a BinaryNumber object.
        """
        self.binary = binary

    def __and__(self, other: "BinaryNumber") -> "BinaryNumber":
        """
        Performs a bitwise AND operation between two BinaryNumber objects.

        """
        return BinaryNumber(self.binary & other.binary)

    def __or__(self, other: "BinaryNumber") -> "BinaryNumber":
        """
        Performs a bitwise OR operation between two BinaryNumber objects.

        """
        return BinaryNumber(self.binary | other.binary)

    def __invert__(self) -> "BinaryNumber":
        """
        Performs a bitwise NOT operation (bit inversion).
        """
        return BinaryNumber(~self.binary)

    def __xor__(self, other: "BinaryNumber") -> "BinaryNumber":
        """
        Performs a bitwise XOR operation between two BinaryNumber objects.
        """
        return BinaryNumber(self.binary ^ other.binary)

    def __eq__(self, other: "BinaryNumber") -> bool:
        """
        Compares two BinaryNumber objects for equality.
        """
        return self.binary == other.binary


bin_num1 = BinaryNumber(0b10001010101010)
bin_num2 = BinaryNumber(0b11111)
bin_num3 = BinaryNumber(0b11000000000000000)
bin_num4 = BinaryNumber(0b1)
bin_num5 = BinaryNumber(0b0)
assert bin_num5 & bin_num4 == BinaryNumber(0b0), "Test1"
assert bin_num5 | bin_num4 == BinaryNumber(0b1), "Test2"
assert bin_num1 ^ bin_num2 == BinaryNumber(0b10001010110101), "Test3"
assert bin_num1 ^ bin_num3 == BinaryNumber(0b11010001010101010), "Test4"
print("OK")
