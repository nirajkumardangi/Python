# Q1. Create a new file “practice.txt” using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java. 
# i like programming in Java. 

with open("7.File-IO/practice.txt", "w") as f:
  f.write("Hi everyone \nwe are learning File I/O")
  f.write("\nusing Java. \ni like programming in Java.")



# Q2. WAF that replace all occurrences of “java” with “python” in above file.
def replace_word():
  with open("7.File-IO/practice.txt", "r") as f:
    data = f.read()
    #replace data
    new_data = data.replace("Java", "PYTHON")
    print(new_data)

  #write new_data
  with open("7.File-IO/practice.txt", "w") as f:
    f.write(new_data)

# replace_word()
  


# Q3. Search if the word “learning” exists in the file or not.
def search_word(word): 
  with open("7.File-IO/practice.txt", "r") as f:
    data = f.read()
    if(word in data):
      print("Found")
    else:
      print("not found") 

# search_word("learning")



# Q4. WAF to find in which line of the file does the word “learning” occur first. Print -1 if word not found.
def check_for_line():
  word = "PYTHON"
  data = True
  line_no = 1
  with open("7.File-IO/practice.txt", "r") as f:
    while data:
      data = f.readline()
      if(word in data):
        print(line_no)
        return 
      line_no += 1 
  print("-1")
check_for_line()