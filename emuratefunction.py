marks = [12,56,32,98,3,2,67,89]
index=0
for mark in marks:
    print(mark)
    index+=1
    if (index ==3):
        print("Hello world")

print("using emurate function: ")

# same program using emurate function
for index, mark in enumerate(marks):
    print(mark)
    if (index ==3):
        print("Hello world")