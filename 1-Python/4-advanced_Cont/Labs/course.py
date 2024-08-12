class Person:
    '''
    Hassan Bahnasy
    '''
    name = ""

    def __init__(self,name):
        print("Constructor is called")
        print(self)
        self.name = name
        print(self.name)

    def greeting(self):
        print("Hello")


    def __str__(self):
        return ("Description of Class Person")

    def __del__(self):
        print("Destructor is called")



Hassan = Person("Hassan")
Hassan.greeting()
print(Hassan)
print(Hassan.__doc__)


class animal:
    name =""
    def __init__(self,name):
        print("1Constructor is called")
        self.name = name

    def eat(self):
        print("eat food")

    def __del__(self):
        print("1Destructor is called")

class cat(animal):
    def __init__(self,name):
        print("2Constructor is called")
        super().__init__(name)

    def sound(self):
        print("Meaouu")

    def __del__(self):
        print("2Destructor is called")
        super().__del__()


mycat = cat("hera")
mycat.eat()
mycat.sound()