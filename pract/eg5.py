li = []
li=[5*x for x in range(1,11)]
for items in li:
    print(items)

with open('table.txt','w') as f:
    f.write(str(li))