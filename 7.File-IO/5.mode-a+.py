# append or add to the file without deleting anything, Open for reading and writing. The file is created if it does not exist. The stream is positioned at the end of the file. Subsequent writes to the file will always end up at the then current end of file, irrespective of any intervening fseek(3) or similar.

file = open("7.File-IO/hello.txt", "a+")
file.write("\nHello John, Good Evening")
file.close()