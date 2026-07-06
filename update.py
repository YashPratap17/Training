import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    # port = 3304,
    user = "root",
    password = "root",
    database = "College_DB"
)

cursor = con.cursor()

print("====== Update Student ======")


student_id = int(input("Enter Student ID to update: "))

name = input("Enter Name: ")
age = int(input("Enter Age: "))
course = input("Enter Course: ")
email = input("Enter Email: ")
city = input("Enter City: ")

query = """
UPDATE students 
SET name = %s, age = %s, course = %s, email = %s, city = %s
WHERE student_id = %s
"""

values = (name, age, course, email, city, student_id)

cursor.execute(query, values)
con.commit()

if cursor.rowcount > 0:
    print("Student Record Updated Successfully")
else:
    print("Student ID not found")

cursor.close()
con.close()