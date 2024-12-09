"""
Purpose:  breakpoint()
        
        - builtin function, introducted in python 3.6
        - same as import pdb; pdb.set_trace()
"""

val_1 = int(input("Enter val_1      :"))
val_2 = int(input("Enter val_2      :"))

# print(val_1, val_2)

# import pdb
# pdb.set_trace()

# import pdb; pdb.set_trace()
breakpoint()

# Multiplication
result =  val_1 * val_2 # val_1 + val_2
print(f"Multiplication   :{result}")


# NOTE: ;(semi-colon) is statement separator