from database import Database

class Admin:
    def __init__(self):
        self.db = Database()
        
    def login(self):
        username = input("Enter Admin Username: ")
        password = input("Enter admin Password: ")

        query = "SELECT * FROM admin WHERE username = %s AND password = %s"
        self.db.execute(query, (username, password))
        admin = self.db.fetchone()

        if admin:
            print("Admin Login Successful!")
            return True # Added return value to track success
        else:
            print("Invalid Admin Credentials")
            return False
        
    def view_all_users(self):
        query = """
        SELECT id, name, email, mobile, username, created_at
        FROM users
        """
        self.db.execute(query)
        users = self.db.fetchall()

        if not users:
            print("No users found")
            return
        
        print("\n========== Users ==========")
        for user in users:
            print(f"""
                  ID          :{user[0]}
                  Name        :{user[1]}
                  Email       :{user[2]}
                  Mobile      :{user[3]}
                  Username    :{user[4]}
                  Created At  :{user[5]}
                  -------------------------------
                  """)
            
    def search_user(self):
        username = input("Enter Username: ")
        query = """
        SELECT id, name, email, mobile, username, created_at
        FROM users
        WHERE username = %s
        """
        # FIXED: Added the trailing comma for the single-element tuple
        self.db.execute(query, (username,))
        user = self.db.fetchone()

        if user:
            print(f"""
                  ID          :{user[0]}
                  Name        :{user[1]}
                  Email       :{user[2]}
                  Mobile      :{user[3]}
                  Username    :{user[4]}
                  Created At  :{user[5]}
                  -------------------------------
                  """)
        else:
            print("User Not found")

    def delete_user(self):
        username = input("Enter Username: ")
        query = "SELECT * FROM users WHERE username = %s"
        self.db.execute(query, (username,))
        user = self.db.fetchone()

        if not user:
            print("User Not found")
            return
        
        choice = input("Delete User (Y/N): ")
        if choice.lower() == "y":
            query = "DELETE FROM users WHERE username = %s"
            self.db.execute(query, (username,))
            
            # ADDED: Make sure to commit the deletion to the database!
            # (Assuming your Database class has a commit method)
            if hasattr(self.db, 'commit'):
                self.db.commit() 
                
            print("User Deleted Successfully")
        else:
            print("Exited")
        
    def total_user(self):
        query = "SELECT COUNT(*) FROM users"
        self.db.execute(query)
        total = self.db.fetchone()
        print(f"Total Users: {total[0]}")

    def dashboard(self):
        while True:
            print("\n----- Admin Dashboard -----")
            print("1. View All users")
            print("2. Search User")
            print("3. Delete User")
            print("4. Total Users")
            print("5. Logout")
            
            # FIXED: Indented the input and if/elif logic inside the loop
            # ADDED: try-except to handle non-integer inputs gracefully
            try:
                choice = int(input("Enter Your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == 1:
                self.view_all_users()
            elif choice == 2:
                self.search_user()
            elif choice == 3:
                self.delete_user()
            elif choice == 4:
                self.total_user()
            elif choice == 5:
                print("Logging Out...")
                break # FIXED: Actually exit the loop when logging out
            else:
                print("Invalid Choice. Please try again.")