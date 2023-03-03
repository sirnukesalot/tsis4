#When we execute the code from the example above the result will be:

#2023-03-03 20:31:44.135581
#The date contains year, month, day, hour, minute, second, and microsecond.

#The datetime module has many methods to return information about the date object.

#Here are a few examples, you will learn more about them later in this chapter:

#Return the year and name of weekday:

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
