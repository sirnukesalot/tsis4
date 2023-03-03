#Define a function with a generator which can iterate the numbers, 
#which are divisible by 3 and 4, between a given range 0 and n.
def result(N):
    for num in range(N):
            if num % 3 == 0 and num % 4 == 0:
                print(str(num) + " ", end = "")
                  
            else:
                pass   
N = 100   
result(N)