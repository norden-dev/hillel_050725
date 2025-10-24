
import string
first_letter, last_letter = input("ВВедите через -").split("-")
letter = string.ascii_letters
print(letter[letter.index(first_letter) : letter.index(last_letter) +1])

