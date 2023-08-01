dict = { "gift" : "flowers",
         "instagram" : "image sharing flatform",
         "Rocket" : "chandrayan3",
         "twitter": "elon musk"
}
print(dict)

#the items that are in dictionary:
print(dict.items())
for a,b in dict.items():
    print(a ,":",b)

#The key value points in the dictionary:
for key in dict.keys():
    print(key)

#For updating the dictionary: 
dict.update({"gift" : "Ballons","Rocket" : "chandrayan2"})
for a,b in dict.items():
    print(dict) 

#sets:
myset = {22,45,78,21}
print(myset)
print(type(myset))
myset.add(89)
print(myset)
myset.remove(22)
print(myset)
print(len(myset))