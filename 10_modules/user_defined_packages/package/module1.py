import sys

# It will affect not this script, but subsequent imports
sys.dont_write_bytecode = True

def hello_world():
    print("Hello from Module1")


if __name__ == "__main__":
    hello_world()
else:
    print(
        f"""
        {__name__    =}
        {__package__ =}
    """
    )