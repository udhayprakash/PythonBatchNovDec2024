"""
Script to demonstrate the import functionality of python code
"""


Greetings = "Good Morning"

def hello_world():
    """ Hello world function"""
    print("Hello world")


if __name__ == "__main__":
    hello_world()
else:
    print(
        f"""
        {__name__    =}
        {__package__ =}
    """
    )



"""
Process to import and reload
 $ python
Python 3.12.1 (main, Sep 30 2024, 17:05:21) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.getcwd()
'/workspaces/PythonBatchNovDec2024/10_modules/user_defined_modules'
>>> os.listdir()
['myscript.py']
>>> import myscript
Hello world
>>> exit()
$ python myscript.py 
Hello world
$ python
Python 3.12.1 (main, Sep 30 2024, 17:05:21) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.listdir()
['myscript.py', '__pycache__']
>>> os.system('ls -ltr')
total 8
drwxrwxrwx+ 2 codespace codespace 4096 Dec 27 17:09 __pycache__
-rw-rw-rw-  1 codespace codespace   90 Dec 27 17:11 myscript.py
0
>>> os.system('ls -ltr __pycache__')
total 4
-rw-rw-rw- 1 codespace codespace 342 Dec 27 17:09 myscript.cpython-312.pyc
0
>>> import myscript
>>> os.system('ls -ltr __pycache__')
total 4
-rw-rw-rw- 1 codespace codespace 387 Dec 27 17:13 myscript.cpython-312.pyc
0
>>> import myscript
>>> os.system('ls -ltr __pycache__')
total 4
-rw-rw-rw- 1 codespace codespace 387 Dec 27 17:13 myscript.cpython-312.pyc
0
>>> import importlib
>>> dir(importlib)
['_RELOADING', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__import__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_bootstrap', '_bootstrap_external', '_imp', '_pack_uint32', '_unpack_uint32', 'import_module', 'invalidate_caches', 'machinery', 'reload', 'sys', 'warnings']
>>> importlib.reload(myscript)

        __name__    ='myscript'
        __package__ =''
    
<module 'myscript' from '/workspaces/PythonBatchNovDec2024/10_modules/user_defined_modules/myscript.py'>
>>> os.system('ls -ltr __pycache__')
total 4
-rw-rw-rw- 1 codespace codespace 523 Dec 27 17:16 myscript.cpython-312.pyc
0
>>> 
"""