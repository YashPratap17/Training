class Account:
    def ac(self):
        print("This Account belongs to Vineet Pandey")
class Savings(Account):
    def save(self):
        print("This is the savings A/C")
class Current(Account):
    def curr(self):
        print("This is the Current A/C")
class Salary(Savings):
    pass
Sal = Salary()

Sal.save()
Sal.ac()