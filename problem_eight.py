import string
import random
#gives the range
n=10

res=''.join(random.choices(string.ascii_uppercase + string.digits,k=n)) #random them
#print result
print(str(res))
