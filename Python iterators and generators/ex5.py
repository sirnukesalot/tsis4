#Implement a generator that returns all numbers from (n) down to 0.
def zero(n):
    for a in range(n,0,-1):
        yield a
        a+=1
g=zero(100)
print(*g)