"""
Purpose: Getting Command-line arguments
"""
import sys

print("__file__", __file__) # absolute path of file
print("sys.argv", sys.argv[0])

'''
$ python b_command_line_args.py 
__file__ /workspaces/PythonBatchNovDec2024/10_modules/02_sys/b_command_line_args.py
sys.argv b_command_line_args.py

 $ python ../02_sys/b_command_line_args.py 
__file__ /workspaces/PythonBatchNovDec2024/10_modules/02_sys/../02_sys/b_command_line_args.py
sys.argv ../02_sys/b_command_line_args.py

$ cd ..
$ python 02_sys/b_command_line_args.py 
__file__ /workspaces/PythonBatchNovDec2024/10_modules/02_sys/b_command_line_args.py
sys.argv 02_sys/b_command_line_args.py

$ cd ..
$ python 10_modules/02_sys/b_command_line_args.py 
__file__ /workspaces/PythonBatchNovDec2024/10_modules/02_sys/b_command_line_args.py
sys.argv 10_modules/02_sys/b_command_line_args.py

'''

print("__file__", __file__.replace("\\", "/"))

assert __file__ != sys.argv[0]
# assert __file__.replace('\\', '/') != sys.argv[0]

print()

print("Number of arguments:", len(sys.argv), "arguments")
print("Arguments List:", list(sys.argv))