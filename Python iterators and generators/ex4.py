#Implement a generator called squares to yield the square of all numbers from (a) to (b). 
#Test it with a "for" loop and print each of the yielded values.
def result(a,b):
    for num in range(a,b):
        yield num**2
c=result(1,100)
print(*c)