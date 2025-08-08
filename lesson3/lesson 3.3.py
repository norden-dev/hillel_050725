lst = [1, 2, 3, 4, 5]
n = len(lst)
half = n // 2

if n == 0:
    results = [[], []]
elif n % 2 == 0:
    results = [lst[:half], lst[half:]]
else:
    results = [lst[:half + 1], lst[half + 1:]]

print(results)