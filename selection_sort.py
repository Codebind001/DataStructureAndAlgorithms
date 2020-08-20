import sys

items = [54, 74, 1, 44, 15, 47, 14, 5, 9]
print("list of items are", items)
for i in range(len(items)):
    min_index = i
    for j in range(i + 1, len(items)):
        if items[min_index] > items[j]:
            min_index = j
    items[i], items[min_index] = items[min_index], items[i]

print("list of sorted items are", items)

# print("Ater sorting array")
# for i in range(len(items)):
#     print("%d" %items[i])