# Getter and Setter methods are used in this

# class Studnet:
#     def __init__(self):
#         self.name = "Yash"
#     def show(self): #this is a public method 
#         print(self.name)
# obj = Studnet()
# obj.show()
# print(obj.name)

# Single underscore is user for protected Method

# class Student:
#     def __init__(self):
#         self._name = "Yash"

#     def show(self):
#         print(self._name)

# obj = Student()
# obj.show()
# print(obj._name) # can be used but it's not recommended 


# Private 

# class Student:
#     def __init__(self):
#         self.__name = "Yash"  #Private variable - Double underscore

#     def show(self):
#         print(self.__name)

# obj = Student()
# obj.show()
# print(obj.__name)


# Getter 

# class Student:
#     def __init__(self):
#         self.__name = "Vineet"

#     def get_mark(self): #getter
#         return self.__name
    
# obj = Student()
# print(obj.get_mark())

# class Student:
#     def __init__(self):
#         self.__marks = 0

#     def set_marks(self,marks):
#         if marks >= 0 and marks <= 100:
#             self.__marks = marks
#         else:
#             print("Invalid No")

#     def get_marks(self):
#         return self.__marks
    
# obj = Student()
# obj.set_marks(65)
# print(obj.get_marks())
# obj.set_marks(150)


# Name mangling Concept 


class Student:
    def __init__(self):
        self.__name = "yash"  #private variable

obj = Student()
print(obj._Student__name)
print(obj.__name) # will throw an error