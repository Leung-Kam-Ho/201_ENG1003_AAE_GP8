pet_list=["dog","bird","rabbit","fish","cat"]
#q1
print(pet_list[0])
print(pet_list[-1])

#q2
print("The price of 3 cars are: {:.2f}, 00{:0>2d}, {:.2f}".format(2690, 1593,7420.5))

#q3
employeeSalary={"John":7500,"Mary":8000,"Peter":6500,"Candy":7000}
print(employeeSalary["Mary"]) #a

employeeSalary["Candy"] = 9000 #b
print(employeeSalary) #b

employeeSalary["David"] = 5000 #c
print(employeeSalary) #c

employeeSalary.pop("Peter") #d
print(employeeSalary) #d

#q4
friendList = ["Betty","","Amy","Crystal","","Lisa"]
def is_not_empty(x):
    return x != ""
newfriendList = filter(is_not_empty,friendList)
friendList = []
for friend in newfriendList:
    friendList.append(friend)
print(friendList)
