# myDict = {x: x**2 for x in [1,2,3,4,5]}
# print (myDict)
#
sDict = {x.upper(): x*3 for x in 'coding'}
for k, v in sDict.items():
    print(k)
    print(v)

'''
for key in sorted(sDict.keys()):
    print (key, sDict[key])

print (sDict)
print (sDict.keys())
print (sDict.values())

for key in sDict:
    print(key)

Dict = {}
print("Empty Dictionary: ")
print(Dict)

Creating a Dictionary
with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

# Creating a Dictionary
# with dict() method
Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)

# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)

'''