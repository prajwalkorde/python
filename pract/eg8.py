with open("this.txt")  as f:
    contain = f.read()
with open("this_new.txt","w") as f:
    f.write(contain)