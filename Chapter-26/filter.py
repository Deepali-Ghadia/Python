# The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.

# filter a list and return only even numbers from the list
def even_number(num):
    if num%2 == 0:
        return num
    
numbers = [x for x in range(0, 20)]

even_numbers = filter(even_number, numbers)
print(even_numbers) # prints object

for i in even_numbers:
    print(i)