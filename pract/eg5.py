class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __add__(self,num):
        return(self.i+num.i,self.j+num.j,self.k+num.k)
    def __mul__(self,num):
        return((self.i*num.i)+(self.j*num.j)+(self.k*num.k))
    def show(self):
        print(f"vecter 1: ({self.i} {self.j}{self.k})")
        print(f"vecter 2: ({self.i} {self.j}{self.k})")

dec1 = vector(1,2,5)
dec2 = vector(10,20,50)
print(dec1+dec2)
print(dec1*dec2)