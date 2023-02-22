# break and continue in loops
# i = 0
# while i < 7:
#     print(i)
#     if i == 4:
#         print("Come out of the loop")
#         break
#     i += 1

for i in range(0,7):
    if i == 4:
        continue
    print(i)
    i += 1


# for loops
for i in range(0, 10):
    print(i+1)
    
    
# iterating over lists
list1 = [1,2,3,4,5,6,7,8,9]
for i in list1:
    print(i)
    
    

# pass statement
# pass is a null statement for when a statement is required by Python syntax (such as within the body of a for orwhile loop), but no action is required or desired by the programmer. This can be useful as a placeholder for codethat is yet to be written.


# iterating over dictionaries
dict1 = {1: 'red', 2: "yellow", 3: "green"}
for key in dict1.keys():
    print(key)
for value in dict1.values():
    print(value)



# Iterating different portion of a list with different step size
num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in num:
    print(num[:])
    print(num[::2])
    print(num[::4])

