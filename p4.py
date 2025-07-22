class employee:
    name = "Wipro"
    salary = 120000
    print("this is part of class.")

    def __init__(self):
        print("this is dunder method.")

ram = employee()
print(ram.name,ram.salary)
