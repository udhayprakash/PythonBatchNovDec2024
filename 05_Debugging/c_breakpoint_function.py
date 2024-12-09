"""
Purpose:  breakpoint()
        
        - builtin function, introducted in python 3.6
        - same as import pdb; pdb.set_trace()
"""


numbers = range(0, 100)

# import pdb; pdb.set_trace()
# breakpoint()

# To Display all even numbers
for each_num in numbers:
    if each_num % 2 == 0: #each_num % 2:
        print(each_num)



# Post Analysis

# python -i SCRIPTNAME.py

