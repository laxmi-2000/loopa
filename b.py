r=0
while r<7:
    c=0
    while c<4:
        if c==0 or (r==6 and c>0):
            print("*",end=" ")
        else:
            print(end=" ")
        c=c+1
    print()
    r=r+1


