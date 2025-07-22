x =[1,2,3,4,5,10,20,30,40,50]
i=0
sum=0
while (i<len(x)):
    sum =sum + x[i]
    x[i]=x[i]+1
print((sum/len(x)))