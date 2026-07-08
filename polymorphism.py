# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog Barks")
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")

# d = Dog()
# d.sound()
# c = Cat()
# c.sound()



# class Dog:
#     def speak(self):
#         print("Dog Barks")
# class Cat:
#     def speak(self):
#         print("Cat meows")

# def animal_sound(animal):
#     animal.speak()
    
# Dog= Dog()
# Cat = Cat()

# animal_sound(Dog)
# animal_sound(Cat)


# class Shape:
#     def area(self):
#         print("Area")

# class Rectangle:
#     def area(self):
#         print("Area of Rectangle")

# class Square(Shape):
#     def area(self):
#         print("Area of Square")

# shapes = [Rectangle(),Square()]
# for shape in shapes:
#     shape.area()

# Operator Polymorphism

# print(10+30)
# print("Yash "+"Pratap")


# Duck Typing

class Student():
    def work(self):
        print("Student is Studying")

class Teacher:
    def work(self):
        print("Teacher is Teaching")

def Perform(person):
    person.work()

S = Student()
T = Teacher()
Perform(T)
Perform(S)

