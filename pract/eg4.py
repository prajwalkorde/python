class complex:
    def __init__(self,r,i):
        self.real = r
        self.imag = i

    def __add__(self,val):
        return complex(self.real+val.real,self.imag+val.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

num=complex(2,5)
num2=complex(3,4)
print(num+num2)