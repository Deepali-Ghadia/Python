import math
x = 1.2334
y = -1.2345

# rounding a value
print(round(x))
print(round(y))


# calculating length of hypotenuse
print(math.hypot(3,4))


# conversion from degree to radians and vice versa
print(math.radians(45))
print(math.degrees(0.7853981633974483))


# calculating power
print(math.pow(2, 10))


# infinities and NAN
positive = math.inf
negative = -math.inf
not_a_number = math.nan
print(positive, negative, not_a_number, sep="\n")


# constants
print(math.pi)
print(math.e)