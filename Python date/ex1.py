#Write a Python program to subtract five days from current date.
from datetime import date, timedelta
dat = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before:',dat)