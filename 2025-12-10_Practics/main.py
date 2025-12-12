import module.makeName as my_name
import module.info as my_info

num = my_family.L

print(num)
for i in num:
    if my_family.myFamilyFirstName[i] == "Kim":
        print(my_family.myFamilyFirstName[i] + " : 누구세요?")
    else:
        print(my_name.myName + "의 가족 " + my_family.myFamilyFirstName[i])
# print(my_info.myInfo)