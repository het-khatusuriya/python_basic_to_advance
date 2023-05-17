# example of functions in python

def calc (a,b):
    sum = (a*b)/(a+b)
    print(sum)



a=9
b=9
calc(a,b)   

def min(a,b):
    if a < b:
        print("a is min")
    else:
        print("b is min")

d = 10
g = 9
min(d,g)


#function arguments example
def average(a,b):
    print("the average is ",(a+b)/2)


average(19,17)