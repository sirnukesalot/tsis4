#The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

#Save this code in the file mymodule.py

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#Import the module named mymodule, and access the person1 dictionary:
import var

a = var.person1["age"]
print(a)