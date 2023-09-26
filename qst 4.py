
# list1=[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# print(list(set(list1)))



list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
result = []

for item in list:
    if item not in result:
        result.append(item)

print(result)
