r=0
while r<7:
    c=0
    while c<5:
        if ((c==0 or c==4) and (r!=0 and r!=6)) or (r==0 or r==6) and (c>0 and c<4):
            print("*",end=" ")
        else:
            print(end="  ")
        c=c+1
    print()
    r=r+1
