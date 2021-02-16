def binary_search(array, key):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = (low+high)//2
        if key == array[mid]:
            return True
        elif key < array[mid]:
            high = mid - 1
        else:
            low = mid + 1


sample_array = [84, 21, 47, 96, 15]
found = binary_search(sample_array, 47)
print('Element 47 is present:\t', found)
