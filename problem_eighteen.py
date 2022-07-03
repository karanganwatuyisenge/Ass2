#function return number times 2
def double(x):
    
    return x*2

#Check if the number is exist in dictionary and return that value in dictionary
def is_exist(dict_,x):
    return x in dict_


def checkNumber():
    n=int(input("How many numbers do you want to enter:"))
    my_dict=dict()
    print("Enter numbers:")
    for i in range(0,n):
        x=int(input())
        if not is_exist(my_dict,x):  #Check if the number is not exist in dictionary 
            #and call the method of double
            my_dict[x]=double(x)

    return my_dict


#display dictionary
diction=checkNumber()
print("My dictionary is:",diction)


