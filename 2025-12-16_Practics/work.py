
a= {"a","b","c"}
b= {"c", "d", "e", "f"}

if len(a) > len(b):
    print("a 리스트길이가 크다.")
else:
    print("b 리스트길이가 크다.")

# -------------------------------------

count1 = 0
count2 = 0
for i in a:
    count1 += 1

for i in b:
    count2 += 1

if count1 > count2:
    print("a가 더 큼")
else:
    print("b가 더 큼")

# -------------------------------------

a = [1,2,3]
b = [1,2,3,4,5,6]
c = ["a","b","c","d","e"]

def makeLen(list):
    count = 0
    for index in list:
        count += 1
    return count-1

if makeLen(a) > makeLen(b):
    print("a가 큽니다.")
else:
    print("b가 큽니다.")
