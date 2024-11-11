"""
Purpose: print() function syntax and usage
    Escapes Sequences
        - characters whose presence is felt, but they were not printed
        \t - tab space
        \n - new line
        \b - overwrites previous character

        r'' - raw string

"""

print("hello world python")
print("hello \tworld \tpython")
print("hello \tworld \npython")


print()

# To ignore the escape sequences
print("hello \tworld \\npython")
print(r"hello \tworld \npython")

print("C:\my\newfolder")
print(r"C:\my\newfolder")
print()



# --------------------
# print(data, sep=' ', end = '\n')

print("hello")  # default end='\n'
print("world")


print("hello", end="\n")
print("world", end="\n")

print("hello", end="___")
print("world")  # default end='\n'


print("hello", end="\t")
print("world")  # default end='\n'


print("hello", "python", 12132, end="\t")  # default sep= ' '
print("world")  # default end='\n'


print("hello", "python", 12132, end="\t", sep=";")
print("world")  # default end='\n'
