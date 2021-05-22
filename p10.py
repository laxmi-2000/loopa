# *** fibonacci series ***
    
num=int(input("enter the number"))
a1,a2=0,1
count=0
while count<num:
    print(a1)
    sum=a1+a2
    a1=a2
    a2=sum
    count+=1




