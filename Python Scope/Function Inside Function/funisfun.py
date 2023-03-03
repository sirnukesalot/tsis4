#As explained in the example above, the variable x is not available outside the function, 
#but it is available for any function inside the function:


#The local variable can be accessed from a function within the function:

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()