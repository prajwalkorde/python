#SUM OF 1ST N NATURAL NUMBER.
def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)
print(f"sum is {sum(6)}")