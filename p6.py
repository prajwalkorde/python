class employee:
    name = "Wipro"
    salary = 120000
    def prnt(self):
        print(f"companey name {self.name}\nsalary is {self.salary}")

class programmer(employee):
    name = "Infosys"
    def show(self):
        print(f"salary is {self.salary}\ncompany name is {self.name}")

a = employee()
a.prnt()
b = programmer()
b.prnt()
b.show()