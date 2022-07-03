#This method help to find te intersection of numbers between two list
def intersection(list1,list2):
    list3=[value for value in list1 if value in list2]
    return list3

#Add numbers in the list one
x=int(input("Enter size of list one:"))
list1=[]
print("Enter elements of first list:")
for i in range(0,x):
    a=int(input())
    list1.append(a)

#Add numbers in the list two
y=int(input("Enter size of list two:"))
list2=[]
print("Enter elements of second list:")
for i in range(0,y):
    b=int(input())
    list2.append(b)

#print list one ,list two and intersection
print("list one is:",list1)
print("list two is:",list2)

print("Intersection of two lists is:",intersection(list1,list2))