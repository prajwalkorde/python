class employee:
    name = "Wipro"
    salary = 120000
    print("this is part of class.")

    @staticmethod
    def prnt():
        a=10
        b=20
        print(f"hello there this is from method.\n c:{a+b}")

ram = employee()
ram.prnt()
