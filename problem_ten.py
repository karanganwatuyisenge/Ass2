#This function helps to return if b is a factor of a
def is_factor(a,b):
    return a%b==0

#input first value and second value
n=int(input("Enter first number:"))
m=int(input("Enter second number:"))

#check condition
if is_factor(n,m):
    print(m,"is the factor of the first number") #if value 1 is factor of value 2 print this message
else:
    print(m,"is not the factor of the first number")#else print this message
