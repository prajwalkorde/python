with open("this_new.txt") as f:
    cont=f.read()
with open("new.txt",'w') as f:
    f.write(cont)