n=int(input("Enter the size of lists:"))
list=[]
#Inputs numbers and add into the list sort them
print("Enter the elements:")
for i in range(0,n):
    x=int(input())
    
    list.append(x)
    list.sort()
print("The maximum number is:",max(list))  #returns maximum number
print("The runner-up number is:",list[-2]) #return runner-up number

