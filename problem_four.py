n=int(input("How many times do you want to insert number in a list:"))
list=[ ]
list1=[]
#input numbers of the list
for i in range(0,n):
    a=int(input("enter elements:"))
    list.append(a)   #Add into the list
    if a%3==0:            #Check the number which is divisible by 3 and append them into a list
      list1.append(a)
print("Our list is:",list)   #Print the whole list
print(len(list1),"number of its elements are multiples of 3")  #print the length of number which is divisible by 3

       
            
        
        