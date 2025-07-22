class emp:
    a=10
    def __init__(self):
        print(f"value of a is {self.a}")
        print(f"hello world from emp")

class emp2(emp):
    b=20
    def __init__(self):
        super().__init__()
        print(f"hello world from emp2")

class emp3:
    c=20
    def __init__(self):
        print(f"hello world from emp3")

n = emp2()
print(f"B is {n.b}")

