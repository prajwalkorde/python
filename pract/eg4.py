n = int(input("Enter a number: "))
bool=False
for i in range(2,n):
    if(n%i==0):
        bool = False
        break
    else:
        bool = True
print(bool)
