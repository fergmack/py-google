import os 

def create_python_script(filename):
  comments = "# Create new python programme"
  with open(filename, "a+") as f:
    f.write(comments)
    print(f.read())
    filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))
