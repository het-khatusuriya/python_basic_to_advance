# tuple datatype in python (immutable)

tup = (1,5,6)
print(type(tup),tup)

print(tup[2])
#tup[2]=5 #  tuples are immutableso it gives error
print(tup)
tup1 = (10,)
print(tup1)

if 5 in tup:
    print("5 is present in tuple name tup")


# tuple methods
tu = (1,5,6,1,2,3,1,4,5,1,5,6)
res = tu.count(1)
print(res)  


