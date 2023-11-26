list_initial = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
list_mul = []
list_ascending = list(list_initial)
list_descending = list(list_initial)
list_ascending.sort()
list_descending.sort(reverse=True)
print(list_ascending)
print(list_descending)
# print(list_initial)
print(list_initial[::2])
print(list_initial[1::2])
for i in list_initial:
    if i % 3 == 0:
        list_mul.append(i)

# list_mul = list(filter(lambda it: it % 3 == 0, list_initial))

print(list_mul)
