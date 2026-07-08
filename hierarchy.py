# class Animal:
#     def eat(self):
#         print("Animal Eats")
# class Dog(Animal):
#     pass
# class Cat(Animal):
#     pass


# # obj = Cat()
# # obj.eat()

# Cat = Cat()
# Cat.eat()
# Dog = Dog()
# Dog.eat()


# class Animal:
#     def eat(self):
#         print("Animal Eats")
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
# class Cat(Animal):
#     def meow(self):
#         print("Cat meows")


# obj = Cat()
# obj.eat()

# Cat = Cat()
# Cat.meow()
# Cat.eat()
# Dog = Dog()
# Dog.bark()
# Dog.eat()



# class A:
#     def __init__(self):
#         print("Construcor of Parent")
# class B(A):
#     pass
# class C(B):
#     pass

# obj1 = B()
# obj2 = C()



# Heirarchy


# class A:
#     def show(self):
#         print("Hello")
# class B(A):
#     pass
# class C(A):
#     pass
# class Z(B,C):
#     pass

# obj = Z()
# obj.show()
# print(Z.mro())


# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")
#         super().show()
# class C(B):
#     def show(self):
#         print("C")
#         super().show()

# obj = C()
# obj.show()
# super.show() checks Child then Parent


class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()
class C(A):
    def show(self):
        print("C")
        super().show()
class D(B,C):  # Left to right, B then C then A
    def show(self):
        print("D")
        super().show()

obj = D()
obj.show()
