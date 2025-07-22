class vector:
    def __init__(self,l):
        self.l = l

    def __len__(self):
        return len(self.l)

num = vector([10,20,5])
print(len(num))