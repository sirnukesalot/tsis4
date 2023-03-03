#If you operate with the same variable name inside and outside of a function, 
#Python will treat them as two separate variables, one available in the global scope (outside the function) \
#and one available in the local scope (inside the function):


#The function will print the local x, and then the code will print the global x:

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)
