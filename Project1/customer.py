from database import Database

class Customer:
    def __init__(self):
        self.db = Database()
        self.con = self.db.connect()
        self.cursor = self.con.cursor()

    def add_customer(self):
        name =input("Enter your name: ")
        mobile = input("Enter Mobile number: ")

        sql = "INSERT INTO customers(customer_name, mobile) VALUES(%s,%s)"
        value = (name, mobile)

        self.cursor.execute(sql,value)
        self.con.commit()

        print("Cusromer Added Sucessfully.")
    
    def view_customer(self):
        sql = "SELECT * FROM customers"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        print("\n ----- Customer List -----\n")

        for row in data:
            print(row)
    
    def add_vehicle(self):
        customer_id = int(input("Enter Customer ID: "))
        vehicle_number = input("Enter Vehicle name: ")
        vehicle_name = input("Enter vehicle Number: ")

        sql = """
        INSERT INTO vehicles (customer_id, vehicle_number, vehicle_name)
        VALUES(%s,%s,%s)
        """
        value = (customer_id, vehicle_name, vehicle_number)

        self.cursor.execute(sql,value)
        self.con.commit()

        print("Vehicle Added Sucessfully!")

    def view_vehicles(self):
        """Display all vehicles with owner name."""
        sql = """
        SELECT 
            vehicles.vehicle_id,
            customers.customer_name,
            vehicles.vehicle_number,
            vehicles.vehicle_name
        FROM vehicles
        INNER JOIN customers ON vehicles.customer_id = customers.customer_id
        """
        self.cursor.execute(sql)
        data = self.cursor.fetchall()

        if not data:
            print("\nNo vehicles found.")
            return

        print("\n----- Vehicle List -----")
        for row in data:
            print(f"ID: {row[0]}, Owner: {row[1]}, Number: {row[2]}, Model: {row[3]}")

        def view_vehicles(self):
            sql = """
            SELECT
            vehicles.vehicle_id,
            vehicles.vehicle_number, 
            vehicles.vehicle_name, 
            customers.customer_name,
            FROM vehicles
            INNER JOIN customers
            ON customers.customer_id = vehicle.customer_id
            """

            self.cursor.execute(sql)
            data = self.cursor.fetchall()

            print("\n----- Vehicle List -----")

            for row in data:
                print(row)

