#super method
class employee:
    def setting(self,name,salary,add):
        self.name = name
        self.salary = salary
        self.add = add
    def prnt(self):
        print(f"companey name {self.name} in {self.add}\nsalary is {self.salary}\n")

class programmer(employee):
    def show(self):
        self.salary
        super().prnt()
        print(f"salary is {self.salary}\ncompany name is {self.name}\n")

sujoy = programmer()
sujoy.setting("wipro",1200000,"buldana")
sujoy.show()
