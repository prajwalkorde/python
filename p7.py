class employee:
    name = "Wipro"
    salary = 120000
    def prnt(self):
        print(f"companey name {self.name}\nsalary is {self.salary}")

class programmer():
    name = "Infosys"
    def show(self):
        print(f"company name is {self.name}")

class coder(employee,programmer):
    name = "TCS"
    def shw(self):
        print(f"name of companey is {self.name}\n")

a = coder()
a.shw()
a.prnt()
a.show()
print(a.salary)