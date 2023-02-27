import os

# joining paths
print(os.path.join('a', 'b', 'c'))

# path component manipulation
print(os.getcwd())
p = os.path.join(os.getcwd(), 'foo.txt')
print(p)


# check if the given path exists
print("Check the existence of path")
path = "E:\Shubhchintak Technology Pvt. Ltd. (Internship)\Training"
print(os.path.exists(path))


# check the type of given path 
print("Check the type of path")
print("Is directory?")
path1_name = "E:\Shubhchintak Technology Pvt. Ltd. (Internship)\Training"
path2_name = "E:\Shubhchintak Technology Pvt. Ltd. (Internship)\Training\Python\Chapter-31\trial_file.txt"
print(os.path.isdir(path1_name))
print(os.path.isdir(path2_name))

print("Is file?")
print(os.path.isfile(path1_name))
print(os.path.isfile(path2_name))