# example of recursion function
#factorial = n * factorial(n-1)

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    


print(factorial(5))




#fibonacci series
def fibo():
        a,b = 0,1
        for i in range(7):
            print(a,end=" ")
            a,b = b,a+b

fibo()