class employee:
    name = "Wipro"
    salary = 120000
    def prnt(self):
        print(f"companey name {self.name}\nsalary is {self.salary}\n")

class programmer(employee):
    name = "Infosys"
    def show(self):
        print(f"salary is {self.salary}\ncompany name is {self.name}\n")

class coder(programmer):
    salary = 1400000
    def sh(self):
        print(f"salary of employee is {self.salary}\n")
        print(f"name of companey is {self.name}")

a = programmer()
b = coder()
b.show()
b.sh()
