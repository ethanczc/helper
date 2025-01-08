'''
Note: Run this section in a non jupyter kernel as it doesnt recognize __file__.
When a script is run in another directory and imports from another, any relative file references is lost.
Therefore, the imported module and its reference to the file is captured and rebuilt.
The calling code can then run the file using absolute paths instead of relative paths.
This code also handles for different platforms and the different use of slashes.
'''

import os

cwd = os.path.dirname(__file__)
print(cwd)

filepath = os.path.join(cwd, 'file.csv')

print(filepath)

# to test this, run this script from a parent directory, and it will still reference to the file properly.