

f=open('readline.txt','r')
while True:
    line=f.readline()
    if not line:
        break
    print(line)