#read write
file = open("7.File-IO/hello.txt", "w")
data = file.write("this is a new line") #overwrite the entire file
file.close()

#read write
file = open("7.File-IO/hello.txt", "a") #append or add to the file without deleting anything
data = file.write("\nmy age is 22")
file.close()

#if file does not exist, "a" or "w" create a file, then write it.
file = open("7.File-IO/sample.txt", "w")
data = file.write("this is created my python") 

file = open("7.File-IO/test.txt", "a")
data = file.write("this is created my PYTHON")
