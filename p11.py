#getters and setters.
class employee:

    @property
    def name(self):
        return f"{self.fname}{self.lname}"
    @name.setter
    def name(self,val):
        self.fname= val.split(" ")[0]
        self.lname= val.split(" ")[1]

ram = employee()
ram.name="prajwal korde"
print(ram.name)
print(ram.fname,ram.lname)
