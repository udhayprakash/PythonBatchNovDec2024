import logging 



logging.debug("This is debug message")
logging.info("This is info message")

# Default logging level is warning
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")
print()




def addition(n1, n2):
    logging.debug("addition function - start")
    return n1 + n2


addition(1, 2)
addition(1, 2)
addition(1, 2)
addition(1, 2)
addition(1, 2)