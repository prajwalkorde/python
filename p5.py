class employee:
    name = "Wipro"
    salary = 120000
    print("this is part of class.")

    def __init__(self,name,salary,lang):
        self.name = name
        self.salary = salary
        self.lang = lang
        print(f"name is {self.name}\nsalary is{self.salary}\nlanguage is {self.lang}")

ram = employee("RAM",1200000,"java")
shyam = employee("SHYAM",1300000,"python")
