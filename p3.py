class employee:
    a=1
    @classmethod
    def show(self):
        print(f"the class attribute of a is {self.a}")

    @property # works with setter.
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter # works with property.
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        

e = employee()
# e.a = 45
# print(e.a)
# # print(employee.a)
e.show()
e.name = "ram rane"
print(e.fname,e.lname)