f = open('File1.txt','r')
while True:
    line = f.readline()
    if not line:
        break
    print(line, end='')