class Person:
    #input your name
    def __init__(self,name):
        self.name=input("Enter your name:")
        
    #Display a greeting and concatenate with your name you entered
    def greet(self):
        print("Hi my name is %s."%self.name)
name=""
person=Person(name)
person.greet()
   
