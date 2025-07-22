class num:
    def __init__(self, n):
        self.number = n

    def __add__(self,nu):
        return self.number + nu.number

n = num(1)
m = num(2)
print(n+m)