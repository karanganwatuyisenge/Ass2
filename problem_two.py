word = input("Please enter your own String : ") #input any string you want to check if it is palindrome or not
word1 = ""
#Processing of reversing from the last character to the first character
for i in word:
    word1 = i + word1 
print("Reverse word :  ", word1)
#Check if the string from reverse is equal to the original string it return the message it is palindrome 
# if it is not equal it is return not palindrome
if(word == word1):
   print("This is a Palindrome String")
else:
   print("This is Not")