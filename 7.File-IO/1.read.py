# text file open -> read -> close
file = open("7.File-IO/hello.txt", "r") #open file, mode: r-read, w-write
data = file.read()                      #read entire file
# data = file.read(5)                   #read only 5 character
print(data)                             #print file
print(type(data))                       #print file-type
file.close()                            #close opened file

#read one line at a time
file = open("7.File-IO/hello.txt", "r")
data = file.readline()  #read one line
print(data)
file.close()


#read multiple line
file = open("7.File-IO/hello.txt", "r")
data = file.readlines()  #read multiple line
print(data)
file.close()