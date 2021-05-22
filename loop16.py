rows=9
i=0
while i<=rows-1:
    j=4
    while j<i:
        print(" ",end=" ")
        j=j+1
    k=i
    while k<=rows-1:
        print("*",end=" ")
        k=k+1
    print()
    i=i+1