n=int(input("Enter size of your list:"))#Input size you want your list will have
list=[]
maxnumber = 0
minnumber=0
#inputs the numbers or elements to be stored in list and print a list
print("Enter numbers:")
for i in range(0,n):
    x=int(input())
    list.append(x)

print("Our list is:",list)
#print the maximum and minimum number stored in the list and print that maximum and minimumnumber
maxnumber=max(list)
minnumber=min(list)
print("Maximu number is:",maxnumber)
print("Minimum number is:",minnumber)

