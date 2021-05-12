"""Working with modules and packages"""

import re


find_functions = []
for function in dir(re):
    if 'find' in function:
        find_functions.append(function)

print(sorted(find_functions))
