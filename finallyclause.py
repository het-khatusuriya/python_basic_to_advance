try:
    l = [1,5,6,7]
    i = int(input("enter the index:"))
    print(l[i])

except:
    print("invalid index")


#finally block is always excecuted

finally:
    print("finally block")