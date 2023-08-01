a = 235
b = "my name is shannu"
c = True
d = 43.45
my_list = [a,b,c,d]
print(my_list)

#Class type: 
print(type(my_list))

#list indexing: a list can be indexed like a string

vowels = ['a', 'e', 'i', 'o', 'i', 'u']
index = vowels.index('e')
print(index)
print(vowels[0:4])

#list methods:
list = [1,3,5,6,2,8,9,103,34,75]
print(list)
list.sort()
print(list)
list.reverse()
print(list)
list.append(200)
print(list)
list.insert(2,12)
print(list)
print(list.pop())
list.remove(34)
print(list)

#Tuples:

numbers= (32,4,3,2)
print(numbers)
print(type(numbers))
#Tuple methods:
evennum = (2,4,4,6,7,8,9,2,6,10,22)
print(evennum.count(4))
print(evennum.index(4))

