import math


def search(arr, ser):
    arr_length = len(arr)
    if arr_length >= 1:
        half_position = math.ceil(arr_length / 2)
        arr_half = int(half_position - 1)
        if arr[arr_half] == ser:
            return ser
        elif arr[arr_half] > ser:
            return search(arr[:arr_half], ser)
        else:
            return search(arr[arr_half + 1:], ser)
    else:
        return -1


input_array = [1, 2]
search_result = search(input_array, 10)
print(f'the result is {search_result}')
