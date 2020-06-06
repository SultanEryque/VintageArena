#empty list

list1 = []

#list of intergers

list2 = [2, 50, 94, 48]

#list with mixed datatypes

list3 = ["Danny", 24, "Murder", 54]

#nested lists

list4 = [10000, ["hacks", 101, "brute", 504],"Flames",[707]]


#accessing a list eg, list3 murder segment

print(list3[2])

#accessing a whole list by slicing operator :

print(list4[:])

#changing a content in a list

list3[0] = 60000

print(list3[0])

#adding to a list

list1.append("Gangstar")

print(list1[:])

#adding multiple items

list2.extend(["Elias", "Samaritan"])

print(list2[:])

#using insert function

list1.insert(1, 600) #inserts 600 in 1st post

print(list1[:])


Neon = ["Gregory", "NIKITA", "Django"]
print(Neon + [5,25,92])
#applicatoon of the + operator 

del Neon[0] #deletes an item from a list
print (Neon)

#pop and remove modulws also work the same way except that you orovide the exact position.
#eg Neon.remove(2) to remove secomd item same.as
#pop with Neon.pop(1)


greyhound = list4.copy()
#copying a list...

print (greyhound)
