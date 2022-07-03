string=[]
#input 4 digits separated with comma
num=[x for x in input("Input 4 digit binary number separated by comma:").split(',')]
for d in num:
    x=int(d,2)
    if not x %5:   #Check if the number is divisible by 5 if it is true append on the string
        string.append(d)
print(','.join(string))
