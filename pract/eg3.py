class employee:
    salary = 1200000

    def sal(self):
        print(f"salary is {self.salary}")

    def incsal(self,i):
        self.inc=i
        print(f"increased by {self.inc}")

    def newsal(self):
        self.nsal=self.inc+self.salary
        print(f"now salary is {self.nsal}")

ram = employee()
ram.sal()
ram.incsal(100000)
ram.newsal()