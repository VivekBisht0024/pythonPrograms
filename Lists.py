my_list = ["apple" , "banana" , "cherry"]
my_list2 = [1,2,3,4,5,6]
my_list3 = [True,False,True]
my_list4 = ["apple" , 100 , True , 40]
print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

print(my_list[0])
print(my_list[-1])

print(my_list4[1:3])

print(my_list[1:])

my_list.append("Watermelon")
print(my_list)

my_list.insert(1,"orange")
print(my_list)


list1 = ["apple" , "mango" , "banana"]
list2 = [1,2,3,4]

list1.extend(list2)
print(list1)

list1.remove("apple")
print(list1)

list1.pop(1)
print(list1)

thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)
