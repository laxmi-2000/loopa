             

rows=5
i=rows
while i>=0:
    j=0
    while j<i:
        print("",end=" ")
        j+=1
    k=i
    while k<=rows-1:
        print(" *",end=" ")
        k+=1
    print()
    i-=1
i=0
while i<=5-1:
    j=0
    while j<i:
        print("",end=" ")
        j+=1
    k=i
    while k<=rows-1:
        print(" *",end=" ")
        k+=1
    print()
    i+=1