set = {2,4,5,6,6} #output = 2,4,5,6 no repeated values
print(set)


s1 = { "cariea", 19, False, 5,9, 19}
print(s1)


for value in s1:
    print(value)



#set methods
s = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))

print("s1:",s1)
print("s2:",s2)
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

