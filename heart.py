a=0
while a<6:
    b=0
    while b<7:
        if (a==0 and b%3!=0) or (a==1 and b%3==0) or (a-b==2) or (a+b==8):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        b=b+1
    print()
    a=a+1