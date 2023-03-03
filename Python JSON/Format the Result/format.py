#The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

#The json.dumps() method has parameters to make it easier to read the result:

#Use the indent parameter to define the numbers of indents:

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))


#You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

#Use the separators parameter to change the default separator:

print(json.dumps(x, indent=4, separators=(". ", " = ")))