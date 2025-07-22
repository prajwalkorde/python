with open("this.txt") as f:
    cont = f.read()
    
with open("this_new.txt") as f:
    cont1 = f.read()

if (cont==cont1):
    print("both are identical.")

else:
    print("not identical.")
