'''
When we want to run an infinite loop in the background (detached from main shell),
there is no way to stop it easily and safely. 
The loop checks a file that carries a 1 or 0,
if 1, the loop runs normally.
if 0, the loop breaks and exits safely.
Make sure the main script and the state file is kept in the same directory.
'''
import time
import os

# include file path referencing 
DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(DIR, 'infinite_state.txt')

def check_state():
    with open(FILE_PATH,"r") as f:
        state = f.read()
        if state == '1': return True
        elif state == '0': return False

def my_function():
    print('my func is running')
    time.sleep(1)

while check_state():
    my_function()