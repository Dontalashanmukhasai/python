#While loop:
i = 0
while(i<=10):
  print(i)
  i+=1

#while using lists
a = [2,3,4,5,6,7,"Shannu"]
i = 0
while(i<len(a)):
   print(a[i])
   i+=1

#for loop:
for i in range(10,100,5):
    print(i)

#printing table 10 using loops:
num = int(input("enter the number:"))
for i in range(10):
   print(f"{num}X{i+1}={num*(i+1)}")

#wite a program to greet all the persons in the list l and which starts with "s":
l = ["shannu","junnu","soham","allu","share"]
for item in l:
   if(item.startswith("s")):
      print(f"good morning{item}")