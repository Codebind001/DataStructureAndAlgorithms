def bubble_sort(items):
    n = len(items)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

items = [40, 50, 10, 30, 20]
print("After Sorting: ", items)
bubble_sort(items)
print("After Sorting: ", items)