# Basics of string formatting
name = "Deepali Ghadia"
city = "Wardha"
state= "Maharashtra"
print("My name is {} and I am from {}, {}.".format(name, city, state) )

# string formatting by specifying indexes
print("My name is {0} and I belong to {2} state {1} city.".format(name, city, state))


# float formatting
floating = 1234.34564322
print("{0:.0f}".format(floating)) # no decimal places
print("{0:.3f}".format(floating)) # upto three decimal places
print("{0:.5f}".format(floating)) # upto five decimal places


