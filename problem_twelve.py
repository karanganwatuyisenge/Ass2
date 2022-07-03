#This function returns the missing values in the second list that are not present in first list
def difference(list1,list2):
    missingvalues=set(list1).difference(list2)
    return missingvalues
#Add numbers in list one
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

#print list one and list two
print("list one is:",list1)
print("list two is:",list2)

#call the method which returns missing values and print them
newlist=difference(list1,list2)

print("Values that are not in the second list is:",newlist)







    
