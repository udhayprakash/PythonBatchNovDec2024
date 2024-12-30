import  sys

sys.dont_write_bytecode = False



import os

print(os.listdir())


import myscript

print(dir(myscript))


print(f""" 
    {myscript.Greetings =}

    {myscript.__name__ =}
    {myscript.__doc__ =}
    {myscript.hello_world =}
    {myscript.hello_world.__doc__ =}

""")

print(callable(myscript.Greetings))  # False
print(callable(myscript.hello_world))  # True
myscript.hello_world()