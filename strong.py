n=int(input("enter the number"))
sum=0
a=n
while n:
    i=1
    b=1
    r=n%10
    while i<=r:
        b=b*i
        i=i+1
    sum=sum+b
    n=n//10
if sum==a:
    print("it is strong number")
else:
    print("is not strong number")
