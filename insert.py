import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    # port = 3304,
    user = "root",
    password = "root",
    database = "College_DB"
)

cursor = con.cursor()

print("====== Add New Student ======")

name = input("Enter Name: ")
age = int(input("Enter Age: "))
course = input("Enter Course: ")
email = input("Enter Email: ")
city = input("Enter City: ")

query = """

INSERT INTO students(name, age, course, email, city)
VALUES (%s,%s,%s,%s,%s)
"""

values = (name, age, course, email, city)

cursor.execute(query, values)
con.commit()

print("Student Added Successfully")

# cursor.close()
# con.close()

query = "SELECT * FROM students"
cursor.execute(query)

records = cursor.fetchall()

print("\n ----- Student Records -----")

for row in records:
    print("ID:",row[0])
    print("Name:",row[1])
    print("Age:",row[2])
    print("Course:",row[3])
    print("Email:",row[4])
    print("City:",row[5])
    print("----------")

cursor.close()
con.close()
