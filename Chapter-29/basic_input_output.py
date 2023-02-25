# reading => opened in read mode(r)
# writing => opened in write(w) or append(a) (at the end of the file) mode

# opening a file
# f1 = open("file1.txt", "r") # read mode
f2 = open("Chapter-29/file1.txt", "w") # write mode


# writing to a file
# write() function -> single line
# writelines() function -> multiple line -> lines are passed as a string
string = "This file is created using python input and output functions"
f2.write(string)
list_of_lines = ["frrthutryiyuhghejdwefjgprtjhioytkhgrd",
                 "gheriotniur erhtioutoi34iy54tui tupiy -57", 
                 "hfiewfieut895unvhge vghw hieto4q3i4tpo3i09o4uiw5r",
                 "hewhfioewutyio45buyi5evtiueutoiewutnv3urneungtf"]
f2.writelines(list_of_lines)


# taking input from a file
with open('Chapter-29/file1.txt', 'w') as fileobj:
    fileobj.write("\n I am Deepali Ghadia")
    
with open('Chapter-29/file1.txt', 'r') as fileobj:
    lines = fileobj.readlines()
    
print(lines)


