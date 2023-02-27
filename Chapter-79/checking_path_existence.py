''' 
os.F_OK Value to pass as the mode parameter of access() to test the existence of path.
os.R_OK Value to include in the mode parameter of access() to test the readability of path.
os.W_OK Value to include in the mode parameter of access() to test the writability of path.
os.X_OK Value to include in the mode parameter of access() to determine if path can be executed
'''

import os
path1 = "E:\Shubhchintak Technology Pvt. Ltd. (Internship)\Training\Python\Chapter-79\checking_path_existence.py"

print(os.access(path1, os.F_OK)) # existence of path
print(os.access(path1, os.R_OK)) # readiability of path
print(os.access(path1, os.W_OK)) # whether it is writable or not
print(os.access(path1, os.X_OK)) #whether it is executable or not


path2 = "E:\Shubhchintak Technology Pvt. Ltd. \Training\Python"
print(os.access(path2, os.F_OK)) # existence of path
print(os.access(path2, os.R_OK)) # readiability of path
print(os.access(path2, os.W_OK)) # whether it is writable or not
print(os.access(path2, os.X_OK)) #whether it is executable or not