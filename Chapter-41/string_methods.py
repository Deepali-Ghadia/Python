string = "Deepali Ghadia"

# changing string to uppercase
print(string.upper())

# changing string to lowercase
print(string.lower())

# capitalizing a string
print(string.capitalize()) #first character is capitalized and other is lower

# titled case version of a string
print(string.title()) # first letter of each word is capital

# swap-case
print(string.swapcase()) #upper converted to lower and vice versa

# string interpolation using str.format()

# useful constants of string module
import string
print(string.ascii_letters) #lowercase+uppercase
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)


# stripping unwanted leading/trailing characters from a string
given_string = "     Deepali Ghadia      " 
print(given_string)
print(given_string.lstrip())
print(given_string.rstrip())
print(given_string.strip())


# split a string based on delimiter
input = "A, B, C, D. E, F, G."
print(input.split()) # bydefault - " "
print(input.split(sep=".")) # separator is .


# Replace all occurrences of one substring with another substring
statement = "The replace() method searches a string for a value or a regular expression. The replace() method returns a new string with the value(s) replaced. The replace() method does not change the original string."
print(statement.replace("string", "statement"))


# Testing what a string is composed of
test = "1,2,3,fd,,fd,fetergergeferg,gev,54v5,6v5,74"
print(test.isalpha()) # true if all the characters are alphabets
print(test.islower())
print(test.isupper())


# join a list of strings into one string
list_of_strings = ["This", "words", "are joined", "to", "form a", "single", "string"]
print(" ".join(list_of_strings))


# counting number of times a substring appears in a string
print(statement.count("string"))


# test the starting and ending characters of a string
print(statement.startswith("The"))
print(statement.endswith("string"))


