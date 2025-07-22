class animal:
    def prt():
        print("class animal")

class pet(animal):
    
    def ptcls(self):
        print("this is a pet")

class dog(pet):
    def bark(self):
        super().ptcls()
        print("bhau bhau!!")

labra=dog()
labra.bark()        

    