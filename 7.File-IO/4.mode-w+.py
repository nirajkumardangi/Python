# w+ : Open for reading and writing. The file is created if it does not exist, otherwise it is overwrite the entire file. The stream is positioned at the beginning of the file.

file = open("7.File-IO/hello.txt", "w+")
file.write("Hello how are you")
file.close()

