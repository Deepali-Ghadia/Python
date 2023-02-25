import os
# # reading a file line by line
# f1 = open("Chapter-30/file1.txt", "r")
# for line in f1:
#     print(line)
    
# # reading from a file using readline() function
# f1 = open("Chapter-30/file1.txt", "r")
# for line in f1:
#     line = f1.readline()
#     print(line)
    
# # getting the full contents of a file
# content = f1.read()
# print(content)


# writing to a file
# f2 = open("Chapter-30/file2.txt", "w")
# f2.write("The contents of this file are written using File I/O functions in python")
# list_of_lines = ["Real data collection and labeling aren’t scalable.",
#                  "Manually labeling real data can sometimes be impossible",
#                  "Real data has privacy and safety issues", 
#                  "Real data is not programmable",
#                  "A model trained exclusively on real data is not performant enough (e.g., slow development velocity)"]
# f2.writelines(list_of_lines)

# f3 = open("Chapter-30/file2.txt", "r")
# data = f3.read()
# print(data)


# checking whether a file or path exists or not using os module
# f1 = open("Chapter-30/file3.txt", "r") # FileNotFoundError: [Errno 2] No such file or directory: 'Chapter-30/file3.txt'
print(os.path.isfile('Chapter-30/file3.txt'))
print(os.path.isfile('Chapter-30/file2.txt'))
print(os.path.isfile('Chapter-30/file1.txt'))


# read a file between a range of lines
import itertools
with open('Chapter-30/file1.txt', 'r') as f:
    for line in itertools.islice(f, 2, 3): # fileobject | no of lines | starting position
        print(line)
