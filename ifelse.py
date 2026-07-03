# age = int(input("Enter Your age: "))
# if age>=18: 
#     print("You are eligible to Vote")
# else:
#     print("You are not eligible to vote")


# num = int(input("Enter a number: "))
# if num%2==0:
#     print("The number is even")
# else:
#     print("The number is odd")

# marks = int(input("Enter Your marks: "))
# if marks>=90:
#     grade = 'A'
# elif marks>=80 and marks <90:
#     grade = 'B'
# elif marks>=70 and marks <80:
#     grade = 'C'
# elif marks>=60 and marks <70:
#     grade = 'D'
# elif marks>=50 and marks <60:
#     grade = 'E'
# else:
#     grade = 'F'

# print("Your grade is " + grade)

# can1= 0
# can2= 0
# can3= 0
# print("Press 1 for Candidate 1")
# print("Press 2 for Candidate 2")
# print("Press 3 for Candidate 3")
# votes = int(input("Select who you want to vote for: "))

# if votes == 1:
#     can1 +=1
# elif votes == 2:
#     can2 +=1
# elif votes == 3:
#     can3 +=1
# else:
#     print("Error Choose the correct option")

# if can1 > can2 and can1 > can3:
#     print("The winner is Candidate 1")
# if can2 > can3 and can2 > can1:
#     print("The winner is Candidate 2")
# if can3 > can1 and can3 > can2:
#     print("The winner is Candidate 3")


# username = input("Enter you username: ")
# password = input("Enter you password: ")

# if username == 'admin':
#     if password == 'admin':
#         print('Login Sucessfull')
#     else:
#         print('Wrong Password')
# else:
#     print('Wrong username')   




# salary = int(input("Enter your Salary: ")) 
# age = int(input("Enter your age: ")) 
# credit_score = int(input("Enter your Credit score: ")) 

# if age >= 25:
#     if salary >=50000 and credit_score >= 700:
#         print("Loan Approved")
#     else:
#         print("Not approved")
# else:
#     print('Not eligible')




# days = input("What is the day Today? ").lower()
# if days == 'saturday' or days == 'sunday':
#     print("Its weekend")
# else:
#     print('Go to Work You aint getting nothing')




# a= 5
# b=10
# c=15
# if a > b and a > c:
#     print("a is greatest")
# if b > a and b > c:
#     print("b is greatest")
# if c > b and c > a:
#     print("c is greatest")



# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# if a > b:
#     print("a is greater")
# else:
#     print("b is greater")



# year = int(input("Enter the Year "))
# if (year% 4 == 0 or year % 100 == 0) or year% 400:
#     print("Its a Leap Year")
# else:
#     print("Not a leap year")



alp = input("Enter the alphabet: ").lower()
if alp in 'aeiou':
    print(alp+ " is a vovel")
else:
    print(alp + ' is a Consonent')
