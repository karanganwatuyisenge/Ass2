class CheckString():   #declaration of class
    def __init__(self):
        self.strings=""
    
    #Allow a user to input any string
    def getString(self):
        self.strings=input("Enter any string:")
    
    #This function return string entered into upper case
    def printString(self):
        print(self.strings.upper())

    
#calling a class and functions in the main
strings=CheckString()
strings.getString()
strings.printString()
