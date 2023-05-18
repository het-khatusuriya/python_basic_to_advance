a = input("enter number to input: ")
print("multiplication of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} * {i} =  {int(a)*i}")
except ValueError:
    print("inavlid input")
except IndexError:

    print("index error")

print("end of program")