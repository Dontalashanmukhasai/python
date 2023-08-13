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

#Nesting list in dictonaries:
Travel_log = {
    "France" : ["Paris","lilly", "dijon"],
    "germany" : ["Berlin", "humberg" , "Stuttgart"]
}
print(Travel_log)

  Travel_log =[
		{
"country": "France":{
"cities_visited": ["Paris", "lilly", "dijon"], "total_visited":12
    
},
		{
  "country": "germany":{
  "cities_visited": ["Berlin", "humberg", "Stuttgart"], "total_visited":5}
    ]print (Travel_log)

#Nesting in a Nesting Dictionary:
Travel_log = {
    "France" : {"cities_visited" : ["Paris","lilly", "dijon"],"total_visited" : 12},
    "germany" : {"cities_visited" : ["Berlin", "humberg" , "Stuttgart"], "total_visited": 5}
}
print(Travel_log)

#sets:
myset = {22,45,78,21}
print(myset)
print(type(myset))
myset.add(89)
print(myset)
myset.remove(22)
print(myset)
print(len(myset))
