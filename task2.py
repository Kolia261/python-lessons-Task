f = open('111.txt', 'r')
K = ["0", "0", "0", "0"]
Name = ["", "", "", ""]
Algebra = ["0", "0", "0", "0"]
Geometry = ["0", "0", "0", "0"]
for i in f:
    L = i.split()
    if L[2] == "8":
        if (int(L[3]) + int(L[4])) > int(K[0]):
            K[0]=str(((int(L[3])+int(L[4]))))
            Name[0] = str(L[0] + " " + L[1])
        if int(L[3]) > int(Algebra[0]):
            Algebra[0] = str(L[3])
        if int(L[4]) > int(Geometry[0]):
            Geometry[0] = str(L[4])
        
    if L[2] == "9":
        if (int(L[3]) + int(L[4])) > int(K[1]):
            K[1]=str(((int(L[3])+int(L[4]))))
            Name[1] = str(L[0] + " " + L[1])
        if int(L[3]) > int(Algebra[1]):
            Algebra[1] = str(L[3])
        if int(L[4]) > int(Geometry[1]):
            Geometry[1] = str(L[4])
    if L[2] == "10":
        if (int(L[3]) + int(L[4])) > int(K[2]):
            K[2]=str(((int(L[3])+int(L[4]))))
            Name[2] = str(L[0] + " " + L[1])
        if int(L[3]) > int(Algebra[2]):
            Algebra[2] = str(L[3])
        if int(L[4]) > int(Geometry[2]):
            Geometry[2] = str(L[4])
    if L[2] == "11":
        if (int(L[3]) + int(L[4])) > int(K[3]):
            K[3]=str(((int(L[3])+int(L[4]))))
            Name[3] = str(L[0] + " " + L[1])
        if int(L[3]) > int(Algebra[3]):
            Algebra[3] = str(L[3])
        if int(L[4]) > int(Geometry[3]):
            Geometry[3] = str(L[4])
f.close()
print("8:", Name[0], int(K[0]))
print("9:", Name[1], int(K[1]))
print("10:", Name[2], int(K[2]))
print("11:", Name[3], int(K[3]))
f = open('111.txt', 'r')
for i in f:
    L = i.split()
    if L[2] == "8":
        if int(Algebra[0]) == int(L[3]):
            output = L[0] + " " + L[1] + " " + L[2]
            print(output)
            output = ''
        if int(Geometry[0]) == int(L[4]):
            outputgeometr = L[0] + " " + L[1] + " " + L[2]
            print(outputgeometr)
            outputgeometr = ''
    if L[2] == "9":
        if int(Algebra[1]) == int(L[3]):
            output = L[0] + " " + L[1] + " " + L[2]
            print(output)
            output = ''
        if int(Geometry[1]) == int(L[4]):
            outputgeometr = L[0] + " " + L[1] + " " + L[2]
            print(outputgeometr)
            outputgeometr = ''
    if L[2] == "10":
        if int(Algebra[2]) == int(L[3]):
            output = L[0] + " " + L[1] + " " + L[2]
            print(output)
            output = ''
        if int(Geometry[2]) == int(L[4]):
            outputgeometr = L[0] + " " + L[1] + " " + L[2]
            print(outputgeometr)
            outputgeometr = ''
    if L[2] == "11": 
        if int(Algebra[3]) == int(L[3]):
            output = L[0] + " " + L[1] + " " + L[2]
            print(output)
            output = ''
        if int(Geometry[3]) == int(L[4]):
            outputgeometr = L[0] + " " + L[1] + " " + L[2]
            print(outputgeometr)
            outputgeometr = ''
