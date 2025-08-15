lst = [0, 1, 0, 2, 4, 8]
res = 0
if len(lst) > 0 :
    a = 0
    b = 0
    while a < len(lst) :
        if a % 2 == 0 :
            b += lst[a]
        a += 1
    res = b * lst[-1]

print(res)