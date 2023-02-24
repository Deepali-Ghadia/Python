# defining a function that accepts list arguments
def sum_of_numbers(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum

result = sum_of_numbers([1, 11, 21, 23, 34, 56, 78, 98, 66])
print(result)