f = open("myfile.txt",'a')
#rb file format to read in binary file

f.write("hello world")
# text = f.read()
# print(text)
f.close()



#shorthand property

with open('myfile.txt','a') as f:
        f.write("hii")