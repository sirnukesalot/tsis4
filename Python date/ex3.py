#Write a Python program to drop microseconds from datetime.
import datetime
d = datetime.datetime.today().replace(microsecond=10)
print(d)