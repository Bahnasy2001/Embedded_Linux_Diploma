class test:
    __m = 10

    def printm(self):
        print(self.__m)

    def __pvfun(self):
        print("hello")

t = test() 
t.printm() # Print 10
#print(t.__m) #ERROR
print(t._test__m) #WORKS # Print 10
t._test__pvfun() #WORKS # Print hello

class MyClass:
    def __init__(self):
        self.__private_variable = 10  # Private member

    def get_private_variable(self):
        return self.__private_variable

    def set_private_variable(self, value):
        self.__private_variable = value

obj = MyClass()
print(obj.get_private_variable())  # Accessing private member
obj.set_private_variable(20)  # Modifying private member
print(obj.get_private_variable())  # Accessing modified private member

class Student:
    name = "unknown"

    def __init__(self):
        self.age = 20
        self._my_variable = 10

    @staticmethod
    def tostring():
        print('student class')
    @property
    def my_variable(self):
        return self._my_variable

    @my_variable.setter
    def my_variable(self, value):
        self._my_variable = value

    @my_variable.deleter
    def my_variable(self):
        del self._my_variable
    


print(Student.tostring()) # Print None if it does not return any thing 
obj = Student()

# Accessing the property like an attribute
print(obj.my_variable)

# Setting the property
obj.my_variable = 20

# Deleting the property
del obj.my_variable