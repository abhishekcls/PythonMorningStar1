# try:
#     #print(a)
#     age=int(input("Enter age: "))
#     print(age)
# except NameError as ne:
#     print(f"{ne.name} is not defined")
# except ValueError:
#     print("Only numbers are allowed")
# except Exception:
#     print("handles all errors")

import logging

try:
    #print(a)
    age=int(input("Enter age: "))
    print(age)
except NameError as ne:
    logging.critical(f"{ne.name} is not defined")
except ValueError:
    logging.error("Only numbers are allowed")
except Exception:
    logging.warning("handles all errors")

print("Done")

'''
Core Logging Levels
Logs are categorized by severity. By default, Python only captures logs at the WARNING level and above. 

Level 	    Value	Purpose
DEBUG	    10	Detailed diagnostic information for developers.
INFO	    20	Confirmation that things are working as expected.
WARNING	    30	Indication of something unexpected or a future problem (default).
ERROR	    40	A serious problem preventing a specific function from running.
CRITICAL	50	A severe failure that may cause the application to crash.

'''