#Lists, tuples, dictionaries, and sets are all iterable objects. 
#They are iterable containers which you can get an iterator from.

#All these objects have a iter() method which is used to get an iterator:

#Return an iterator from a tuple, and print each value:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#Even strings are iterable objects, and can return an iterator:

#Example
#Strings are also iterable objects, containing a sequence of characters:

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))