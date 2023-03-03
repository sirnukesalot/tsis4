#There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

#List all the defined names belonging to the platform module:

import platform

x = dir(platform)
print(x)

#Note: The dir() function can be used on all modules, also the ones you create yourself.