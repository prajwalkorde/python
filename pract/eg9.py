# n1 = int(input("Enter a number: "))
# for i in range(n1+1):
#     for j in range(i):
#         print("*",end=" ")
#     print(" ")

n1 = int(input("Enter a number: "))
for i in range(1,n1+1):
    if(i==1 or i==n1):
        print("*"*n1,end="")
    else:
        print("*",end="")
        print(" "*(n1-2),end="")
        print("*",end="")
    print("")

