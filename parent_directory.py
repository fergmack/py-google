# The parent_directory function returns the name of the directory that's located just above the current working directory. Remember that '..' is a relative path alias that means "go up to the parent directory". Fill in the gaps to complete this function

import os 

def parent_directory():
  # Create relative path for parent 
  relative_path = os.path.join(os.getcwd(), '..')

  # Use abspath for absolute parent path
  return os.path.abspath(relative_path)

print(parent_directory())
