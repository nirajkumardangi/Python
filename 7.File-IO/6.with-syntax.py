#with keyword in read mode
with open("7.File-IO/hello.txt", "r") as f:
  data = f.read()
  print(data)
  #with keyword automatically close the file


#with keyword in write mode
with open("7.File-IO/hello.txt", "w") as f:
  f.write("written by alex by using with keyword")
