# copying a dictionary : shallow copy

dict1 = {1:"A", 2: "B", 3: "C"}
dict2 = dict1.copy()
print("Before Changing")
print(dict1)
print(dict2)
dict1[1] = "AAAAA"
print(dict1)
print(dict2)


# # performing a deep copy using deepcopy function from copy module
# # In case of nested lists, it is desirable to clone the nested lists as well. This action is called deep copy.
import copy
# dict2 = copy.deepcopy(dict1)
# print(dict1 is dict2)


# # performing shallow copy of a list => change in original ist affects the copied list as well
alpha = ["A", "B", "C", "D", "E"]
beta = alpha
print("Before changing element in alpha list")
print(alpha)
print(beta)
alpha[0] = "Z"
print("After changing element in alpha list")
print(alpha)
print(beta)


# perfroming deepcopy of a list
print("Performing deep copy")
a = [1, 2, 3, 4, 5, 6]
b = copy.deepcopy(a)
print("Before changing element in first list")
print(a)
print(b)
a[0] = 999
print("After changing element in first list")
print(a)
print(b)