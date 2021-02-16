def linear_search(array, key):
    position = 0
    flag = False
    while position < len(array) and not flag:
        if array[position] == key:
            flag = True
        else:
            position += 1
    return flag


sample_array = [84, 21, 47, 96, 15]
found = linear_search(sample_array, 47)
print('Element 47 is present:\t', found)
