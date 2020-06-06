integers = {500, 1500}
#set of integers

print (integers)

data = {600, "Lionel", "champions", (400, 500, 20)}
#mixed data sets

print (data)


integers.add(1000) #adds 1000 to the set(single)
print (integers)

data.update("Finch", "Jack Bauer") #adds multiple data to a set
print (data)

data.remove(600) #removes data in a set
print (data)


data.clear() #empties a set
print (data)

numbers = {300, 800}

union = integers | numbers #combines two sets

print (union)

union2 = integers.union(numbers) #also combines two sets

print (union2)


numbers.add(1000)
section = integers & numbers #gets the intersection

print (section)

