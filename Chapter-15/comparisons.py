# chain comparison
a = 23
b = 15
c = 89
d = 23
print(a > b < c == d)


# comparison by is vs "=="
# == compares the values
# compares the identities i.e ids of both the elements
print(a==d)
print(id(a))
print(id(d))
print(a is d) # bcoz both variables are referring to same value


