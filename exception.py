# print("One")
# print("Two")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Division by zero not allowed")



# print("Welcome to the Program")

# a = int(input("Enter the first Number"))
# b = int(input("Enter the Second Number"))

# try:
#     result = a/0
#     print("Division by Zero Not Allowed")
# except ZeroDivisionError:
#     print("Division By Zero Not allowed")


# try:
#     age = int(input("Enter Age"))
# except:
#     print("Enter Valid Age")

# try:
#     a = int(input("Enter a Value: "))
#     b = int(input("Enter next Value: "))
#     print(a/b)
# except ValueError:
#     print("Enter Valid Value")
# except:
#     print("Division by Zero not Allowed")


# Else Block

# try:
#     a = int(input("Enter a Value: "))
#     b = int(input("Enter next Value: "))
#     print(a/b)
# except ValueError:
#     print("Enter Valid Value")
# except:
#     print("Division by Zero not Allowed")

# else:
#     print("Division Sucessfully")

# Finally Block

# try:
#     a = int(input("Enter a Value: "))
#     b = int(input("Enter next Value: "))
#     print(a/b)
# except ValueError:
#     print("Enter Valid Value")
# except:
#     print("Division by Zero not Allowed")

# else:
#     print("Division Sucessfully")

# finally:
#     print("Program Executed Sucessfully")


# try:
    # print(10//2)
    # print(10.0//2)
    # print(10//2.0)
#     print(10.0//2.0)
# except:
#     print("Error")
# else:
#     print("Not Error")
# finally:
#     print("Completed")



# Raise Error

# age = int(input("Enter Your Age: "))
# if age < 18:
#     raise ValueError("Age Must be Above 18")
# print("Eligible")


# AS keyword

# try:
#     print(10/0)
# except ZeroDivisionError as e:
#     print(e)


# Make a Calculator using Try and except block doing all the Variations

print("===== Welcome to Calculator =====\n")

try:
    a = int(input("Enter a Value: "))
    b = int(input("Enter next Value: "))
    
except ValueError:
    print("Enter Valid Value")

cal = input("Select +,-,*,/ for the Calculations: \n")

if cal == '+':
    print(a+b)
elif cal == '-':
    print(a-b)
elif cal == '*':
    print(a*b)
elif cal == '/':
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Division By zero Not Allowed")


else:
    print("Wrong Choosing")