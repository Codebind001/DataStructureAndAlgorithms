def binary_search(items, low, high, key):
    if high >= low:
        mid = (high + low) // 2

        if items[mid] == key:
            return mid
        elif items[mid] > key:
            return binary_search(items, low, mid-1, key)
        else:
            return binary_search(items, mid+1, high, key)
    
    else:
        return -1

items=[2,3,4,5,6,7,8,9]
key=8

result= binary_search(items,0,len(items)-1,key)

if result != -1:
    print("Element found at index ", str(result))
else:print("Element not found")