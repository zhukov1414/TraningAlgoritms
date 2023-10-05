def binary_search(array, search_value):
    left  = 0
    right = len(array) - 1

    for _ in range(len(array)):
        mid = (left + right) // 2

        if  array[mid] == search_value:
            return mid
        elif array[mid] < search_value:
            left = mid + 1
        else:
            right = mid - 1

    return -1 






print(binary_search([1, 3, 5, 7, 9, 11, 13, 15, 17], 7))