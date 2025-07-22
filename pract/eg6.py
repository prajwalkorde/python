#factorial of a given number.
n = int(input("Enter any number: "))
for i in range(2,n):
    n*=i
print(f"factorial is : {n}")