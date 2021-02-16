def binary_search(array, key, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if key == array[mid]:
            return True
        elif key < array[mid]:
            return binary_search(array, key, low, mid - 1)
        else:
            return binary_search(array, key, mid + 1, high)


sample_array = [84, 21, 47, 96, 15]
found = binary_search(sample_array, 47, 0, 5)
print('Element 47 is present:\t', found)
