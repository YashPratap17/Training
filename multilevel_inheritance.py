# class Father:
#     def house(self):
#         print("Give it to the Son")
        
# class Mother:
#     def jewellry(self):
#         print("Give it to Son's wife")
# class Son(Father,Mother):
#     pass

# obj = Son()
# obj.house()
# obj.jewellry()


# class Relative:
#     def money(self):
#         print("Here is some money")

# class Son:
#     def thank(self):
#         print("Thanks")
        
# class Mother(Relative,Son):
#     pass

# obj = Mother()
# obj.money()
# obj.thank()


# class Relative:
#     def money(self):
#         print("Here is some money")

# class Son:
#     def thank(self):
#         print("Thanks")

# class Mother(Relative,Son):
#     def give(self):
#         print("Give me Your money so that i can save it for you")

# obj = Mother()

# obj.money()
# obj.give()
# obj.thank()
    

# class Father:
#     def __init__(self):
#         print("Father Constructor Call")
# # class Mother():
# class Mother:
#     def __init__(self):
#         print("Mother Constructor Call")
# class Son(Father,Mother):
#     pass

# obj = Son()
# print(Son.mro())



# class Father:
#     def __init__(self):
#         # call next __init__ in MRO
#         print("Father Constructor Call")
#         super().__init__()
# class Mother():
#     def __init__(self):
#         print("Mother Constructor Call")
#         super().__init__()
# class Son(Father,Mother):
#     def __init__(self):
#         # follow MRO and let each constructor run via super()
#         super().__init__()

# obj = Son()
# print(Son.mro())


# class A:
#     def show(self):
#         print("A")
# class B:
#     def show(self):
#         print("B")
# class C(A,B):
#     pass



# class Animal:
#     def sound(self):
#         print("Animal Sound")
# class Dog(Animal):
#     def eat(self):
#         print("Dog Eats")
# class Puppy(Dog):
#     def sleep(self):
#         print("Puppy Sleeps")
# p = Puppy()
# p.sound()
# p.eat()
# p.sleep()

# class Grandfather:
#     land = 20
# class Father(Grandfather):
#     house = 2
# class Son(Father):
#     bike = "RE Bullet"

# s = Son()
# print(s.land)
# print(s.house)
# print(s.bike)

# class Uni:
#     affiliation = 10
# class College(Uni):
#     schools = 5
# class School(College):
#     students = 1000

# s = School()
# print(s.affiliation)
# print(s.schools)
# print(s.students)


# class A:
#     def __init__(self):
#         print("Constructor of A")
# class B(A):
#     pass
# class C(B):
#     pass
# c = C()

# class A:
#     def __init__(self):
#         print("Constructor of A")
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("Constructor of B")
# class C(B):
#     def __init__(self):
#         super().__init__()
#         print("Constructor of C")

# obj = C()

# Look the output is coming from the top to bottom 