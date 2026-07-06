import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    # port = 3304,
    user = "root",
    password = "root",
    database = "College_DB"
)

cursor = con.cursor()

student_id = int(input("Enter the ID to delete: "))

query = "DELETE FROM students where student_id=%s"

cursor.execute(query,(student_id,))

con.commit()

if cursor.rowcount >0:
    print("Student Record deleted Sucessfully")
else:
    print("Student ID not Found")

cursor.close()
con.close()