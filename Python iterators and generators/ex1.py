#Create a generator that generates the squares of numbers up to some number N.
def squares(N):
    for i in range(N): 
        yield i**2
n=int(input())
a=squares(n)
print(*a)