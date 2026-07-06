import mysql.connector

class Database:
    def connect(self):
        con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "garage"
        )

        return con