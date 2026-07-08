# class Animal:
#     def sound(self):
#         print("Animal Makes Sound")

# class Dog(Animal):
#     def bark(self):
#         print("Dog Barks")

# d = Dog()
# d.sound()
# d.bark()


# class Parent:
#     def money(self):
#         print("The money will be given to my sons")

# class Child(Parent):
#     def father(self):
#         print("I will inherit my Father")
# a = Child()
# a.father()
# a.money()


# class Person: #person -> Class variable
#     name = "Yash"
#     def show(self):
#         print("name",self.name)
# class Student(Person):
#     pass

# a = Student()
# a.show()

# class Teacher:
#     mark = 50
#     def marks(self):
#         print("Marks: ",self.mark)
# class Student(Teacher):
#     def my_marks(self):
#         print("My marks",end="")

# a = Student()
# a.marks()
# a.my_marks()


# class Father:
#     price = 5000
# class Son(Father):
#     bike = "Bullet"

# c = Son()
# print(c.price)
# print(c.bike)


class Marks:
    mark = 90
class Student(Marks):
    m = Marks()
    def my_marks(self):
        if m.mark() > 80:
            print("Pass")
        print("Fail")

s = Student()
s.my_marks()