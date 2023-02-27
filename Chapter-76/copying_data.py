
# performing shallow copy of a list => change in original ist affects the copied list as well
print("------Performing shallow copy------")
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
print("------Performing deep copy------")
a = [1, 2, 3, 4, 5, 6]
b = copy.deepcopy(a)
print("Before changing element in first list")
print(a)
print(b)
a[0] = 999
print("After changing element in first list")
print(a)
print(b)