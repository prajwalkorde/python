class twodv:

    def __init__(self,i,j):
        self.i =i
        self.j =j

    def prt(self):
        print(f"2d vector:\n {self.i}i + {self.j}j")
    
class threedv(twodv):

    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def prt2(self):
        print(f"3d vector:\n {self.i}i + {self.j}j + {self.k}k")

vec1=twodv(10,20)
vec1.prt()
vec2=threedv(1,2,3)
vec2.prt2()