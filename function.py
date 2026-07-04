# def welcome():
#     print("Hello World!")

# welcome()

# def Yash():
#     print("Hello I'm Yash!")
# Yash()

# def yash():
#     Name = input("Enter Your name: ")
#     Roll = int(input("Enter Your Roll no: "))
#     Year = int(input("Enter Your Year of Joining: "))

#     print(Name)
#     print(Roll)
#     print(Year)

# yash()


# def one():
#     print("One")

# def two():
#     one()
#     print("two")

# two()

# def greet(name):
#     print("Hello", name)

# greet("Yash")
# greet("Vineet")
# greet("Vansh")


# def sq(num):
#     print("The Square of",num ,"is",num*num)


# sq(5)
# sq(6)
# sq(7)

# def table(num):
#     for i in range(1,11):
#         print(num,"x",i ,"=",num*i)

# numb = int(input("Enter the number: "))
# table(numb)


# Calculator using function +,-,*,/

# def calculator():
#     a = float(input("Enter the first number: "))
#     b = float(input("Enter the second number: "))
#     par = input("Select the sign for +,-,*,/: ")
#     if par == '+':
#         print("The sum is", a + b)
#     elif par == '-':
#         print("The difference is", a - b)
#     elif par == '*':
#         print("The product is", a * b)
#     elif par == '/':
#         if b == 0:
#             print("Division by zero not allowed!!")
#         else:
#             print("The Division is", a / b)
#     else:
#         print("Wrong Choosing")

# calculator()



# def std(name,age):
#     print(name)
#     print(age)

# std(name ="Yash",age = 22)



# def country(name,nation="India"):
#     print(name,nation)

# # country("Abhi")
# country("Abhi","Us")


# def login(name, pwd = 'admin'):
#     print(name,pwd)

# n = input("Enter Your name: ")
# m = input("Enter Your Password: ")
# login(n,m)


# *args -> returns in Tuple

# def number(*num):
#     print(num)

# number(10)
# number(10,20)
# number(10,30,4)
# number(10,151,94,6,45)


# **kwargs -> Returns is Dictionary

# def info(**data):
#     print(data)

# info(name='Yash',age = 22)
# info(name='Vineet',age = 27)

# def square(num):
#     # return num*num
#     print(num*num)

# print(square(5))

# def nums(a):
#     if a%2 == 0:
#         return print("The Number is even")
#     else:
#         return print("Odd")
    
# num = int(input("ENter a number: "))
# print(nums(num))

def cal(a,b):
    add = a+b
    sub = a-b
    mul = a*b

    return add,sub,mul
x,y,z = cal(20,10)
print(x)
print(y)
print(z)