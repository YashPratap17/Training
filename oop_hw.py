# Single inheritance

# class A:
#     def a_name(self):
#         print("Class A")
# class B(A):
#     def b_name(self):
#         print("Class B")

# obj = B()
# obj.a_name()
# obj.b_name()

# class A:
#     def __init__(self):
#         print("Hello A")
#     def _protect(self):
#         print("Protected Self")

# obj = A()
# obj._protect()


from abc import ABC

class A(ABC):
    @abs

