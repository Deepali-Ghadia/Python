import re
text = "Regular expressions are combinations of characters that are interpreted as rules for matching substrings. For instance, the expression 'amount\D+\d+' will match any string composed by the word amount plus an integral number, separated by one or more non-digits, such as:amount=100, amount is 3, amount is equal to: 33, etc."

print(len(text))

# matching the beginning of a string
output1 = re.search("^Reg", text)
print(output1) # returns match object if match occurs else None
# <re.Match object; span=(0, 3), match='Reg'> | span specifies the position of search

output2 = re.search("c.$", text)
print(output2)
# <re.Match object; span=(321, 323), match='c.'>


# findall() function
output3 = re.findall("ch", text)
print(output3)  # returns a list containing all the matches
# returns empty list if no match is found


# split function
output4 = re.split("ch", text)
print(output4) # provides a list where the text is splitted wherever a match occurs

# control the number of splits
output5 = re.split("ch", text, 2) # will be splitted at first two occurences
print(output5)


# replacing the text using sub function
output6 = re.sub("ch", "AA", text)
print(output6) # returns string with the replaced characters

# control the number of replacements by specifying the count parameter
output7 = re.sub("ch", "AAAAAAAAAAAAAAAAAAAa", text, 1)
print(output7)


