from collections import Counter
string=input("Enter string:") #Enter string
character=input("Enter character you want to know the times it appear in your string:")
count=Counter(string)
#display times your character appear in the string
print(count[character])