import logging
import sys

# Fixing the level of severity
logging.basicConfig(level=logging.DEBUG)

logging.debug("This is a debug1")


# To disable the logging completely

# Method 1
# # logging.disable(sys.maxint) # Python 2
# logging.disable(sys.maxsize)  # Python 3

# Method 2
logging.getLogger().disabled = True

logging.debug("This is a debug2")
logging.info("This is a info2")
logging.warning("This is a warning2")
logging.error("This is a error2")
logging.critical("This is a critical2")
print()