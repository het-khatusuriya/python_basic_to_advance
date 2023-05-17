l = [3,5,6]
# basic example of list
print(l)
print(type(l))


# orderly manner
print(l[0])
print(l[2])
print(l[-1])
print(l.count('3'))
print(len(l))

# it contains string also
l1 = [3,5,6,"hello","hii"]
print(l1[4])
print(l1[2-4])  #2-4=-2s
print(l1[2:4])


lst= [i*i for i in range(10) if i%2==0]
print(lst)


#list methods

lis = [2,3,4]
print(lis)
lis.append(9)
print(lis)
print(lis.sort())
print(lis.index(3))
print(lis.reverse)
print(lis.count(3))
print(lis.pop())
m =lis.copy()
print(m.clear)
