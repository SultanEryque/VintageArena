#same as set but only difference is it has a key...

dict1 = {1: 'Relays', 2: 'Trojan'}
#dictonary with integer keys

#dictionary with mixed keys
dict2 = {'name': 'Jack', 1: 700, 'Age': 60}
print (dict2)


print (dict2['name']) 
#accessing dictionary is done by key values

#method to of accessing a value
value = dict2.get('Age')
print ("The Age is", value)

#adding to a dictionary
dict1['scan'] = 'Loading'
print (dict1)

#updating  a key in a dictionary
dict1[2] = 'Accomplished'
print (dict1)
