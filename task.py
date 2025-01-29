c=0
f=open("1.txt", "r")
for i in f:
    s=i[-5:-1]
    family=i[0:10]
    if int(s) < 1978:
        c +=1
        print(family)
f.close()
a = int(input())
b = int(input())
f=open("1.txt", "r")
for i in f:
    s=i[-5:-1]
    inf=i
    if int(s) < b and int(s) > a:
        print(inf)
f.close()

