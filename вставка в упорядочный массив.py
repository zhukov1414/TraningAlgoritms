def sum_two_smallest_numbers(numbers, n):
    for i in range(len(numbers)):
        if numbers[i] > n:
            numbers.insert(i, n)
            return numbers
    numbers.append(n)
    return numbers



print(sum_two_smallest_numbers([3, 17, 80, 202], 75))
