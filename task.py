c=0
f=open("1.txt", "r")
for i in f:
    s=i[-5:-1]
    L=i.split()
    if int(s) < 1978:
        c +=1
        print(L[0])
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

