#1. Class definatio
class Parent():
    #1.1 property/value
    bloodGroup='' #define property


    #1.2 constructor is a special function/method
    def __init__(self,bg=''): #self is internal object
        if bg != '':
            self.bloodGroup = bg #property value initialization  
        else:
            self.bloodGroup ='ab+ve'

    #1.3 method/function
    def myMethod(self):
        print(f'My Blood Group Is {self.bloodGroup}')


#2. Create Class Object
ceo = Parent('o+ve')
     #2.1 call the method with class object
ceo.myMethod()     