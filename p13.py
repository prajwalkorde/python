class xyz:
    def __init__(self,num):
        self.nv = num
    def __sub__(self,nn):
        return self.nv - nn.nv
r = xyz(30)
j = xyz(20)

print(r-j)
