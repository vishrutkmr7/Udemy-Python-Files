# Doing some file handling stuff here
newfile = open("newfile.txt", "w+")
# Read: r, write+ = w+
string = "This is the content to be written in the text file"
newfile.write(string)
