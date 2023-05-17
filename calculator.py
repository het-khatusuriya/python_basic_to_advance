#calculator using python
num1 = input("Enter 1st number: ")
print("Number 1:", num1)
num2 = input("Enter 2nd number: ")
print("Number 2:", num2)

var = input("Enter operation")

if var == "add":
         # add
    add = int(num1) + int(num2)
    print(add)

elif var == "sub" :
    #sub
    sub = int(num1) - int(num2)
    print(sub)

elif var == "mul" :
    #mul
    mul = int(num1) * int(num2)
    print(mul)


elif var == "div" :
    #div
    div = int(num1) / int(num2)
    print(div)

else:
    print("WRONG CHOICE")

