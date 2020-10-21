def exponential_search (array, searched, segment, array_length):
    if segment > array_length:
        indexInit = int((segment / 2) - 1)
        for i in range(indexInit, array_length):
            if array[i] == searched:
                return i
        return -1

    index = segment -1
    val = array[index]
    if val == searched:
        return index
    elif (val > searched) & (segment == 1):
        return -1
    elif val < searched:
        return exponential_search(array, searched, segment * 2, array_length)



arr = [10, 20, 40, 45, 55]
result = exponential_search(arr, 20, 1, len(arr))
if result == -1:
    print("Element is not present at index", result)
else:
    print("Element is present at index", result)

