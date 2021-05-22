
row=5
i=row
while i>=1:
    j=row
    while j>i:
        print(" ",end=" ")
        j-=1
    k=1
    while k<=i:
        print("*",end=" ")
        k+=1
    print()
    i-=1