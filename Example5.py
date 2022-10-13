# Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение [1, 2, 2, 3]

list1 = [1, 2, 3, 2, 0]
list2 = [5, 1, 2, 7, 3, 2]
list3 = []
for item in list1:
    if item in list2:
        list3.append(item)
print(list3)