#Example of an object
#Merci Knupp
class TestObject(object):
    
    def __init__(self, name, number):
        self.name = name
        self.number = number
#################################
    def doSomething(self):
        if self.number > 100:
            print("above 100")
        else:
            print("Below 100")
        return self.number
    
#################################