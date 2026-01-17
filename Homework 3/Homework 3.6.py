import re


class User:
    """
    Represents a user with first name, last name, and email address.
    """

    def __init__(self, first_name: str, last_name: str, email: str) -> None:
        """
        Initializes a User instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @property
    def first_name(self) -> str:
        """
        Returns the user's first name.
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        """
        Sets the user's first name.
        """
        self.__first_name = value.strip()

    @property
    def last_name(self) -> str:
        """
        Returns the user's last name.
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        """
        Sets the user's last name.
        """
        self.__last_name = value.strip()

    @property
    def email(self) -> str:
        """
        Returns the user's email address.
        """
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        """
        Sets the user's email address after validation.
        """
        email_value = value.strip()
        if not User.is_valid_email(email_value):
            raise ValueError("Invalid email format")
        self.__email = email_value

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Validates the email address format.
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))


user1 = User("Ivan", "    Ivanov   ", "ivanov@mail.com")
print(user1.first_name)
print(user1.last_name)
print(user1.email)
