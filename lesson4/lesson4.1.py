lst = [0, 1, 0, 12, 3]

count = 0
i = 0
while i < len(lst) :
    if lst[i] == 0 :
        lst.pop(i)
        count += 1
    else :
        i += 1

for _ in range(count) :
    lst.append(0)

print(lst)