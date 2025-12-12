import nameList

i = 0
j = 0
L = []
while i < len(nameList.myFamilyFirstName)-1:
    while j < len(nameList.myFamilyLastName)-1:
        L.append(nameList.myFamilyFirstName[i] + " " + nameList.myFamilyLastName[j])
        j += 1
    j = 0
    i += 1

print(L)