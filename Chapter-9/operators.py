# simple mathematical operators
import math
import operator

a = 10
b = 20
c = 23
d = 2
l1 = [1,2,3]
l2 = [4,5,6]
t1 = (1,2,3)
t2 = (3,4,5)

# division
print(a/b)
print(a/c)
print(a/d)
# print(a//b)gives integer value by taking floor value
print(a//c)
print(a//d)


# addition
print(a+b)
print(l1 + l2)
print(t1 + t2)


# Exponentiation
a1 = 2
a2 = 3
print(a1**a2)
print(math.pow(2,3)) # gives answers in float
print(operator.pow(2,3)); # gives answer in integer value


# Trigonometric Functions
print(math.sin(90)) # returns sin(90) in radians
print(math.hypot(3,4)) # calculates the hypotenuse

# Inplace operations
a += 1
print(a)
a -= 1
print(a)


# Modulus
print(10%5)
print(operator.mod(10,5))