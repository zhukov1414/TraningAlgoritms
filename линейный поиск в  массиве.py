def sum_two_smallest_numbers(numbers, n):
    for i in range(len(numbers)):
        if numbers[i] == n:
            return i
    if numbers[i] != n:
        return 'Not value'



print(sum_two_smallest_numbers([3, 17, 80, 202], 17))
