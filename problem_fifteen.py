
n=int(input("How many times you want to input?"))
dict={}
#Enter string
print("Enter strings:")
for i in range(0,n):
    x=input()
    if x in dict:  #Check if the string is already in dictionary if it is true add one
        dict[x]+=1
    else:
        dict[x]=1 #if the string does not exist in dictionary assign 0ne

#print dictionary
for key in dict:
    print('{',key,':',dict[key],end=',' +'}')
    
