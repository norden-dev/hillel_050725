import random
length = random.randint(3, 10)
lst = []

for _ in range(length) :
    lst += [random.randint(0, 100)]

new_lst = [lst[0], lst[2], lst[-2]]

print("Початковий:", lst)
print("Новий:", new_lst)