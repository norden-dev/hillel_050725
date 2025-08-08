lst = [1, 2, 3, 4, 5]
if len(lst) > 1:
    lst = [lst[-1]] + lst[:-1]

print(lst)