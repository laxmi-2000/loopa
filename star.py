

rows=5
i=1
while i<=rows:
    j=i
    while j<rows:
        print(" ", end=" ")
        j+=1
    k=1
    while k<=i:
        print("*", end=" ")
        k+=1
    print()
    i+=1


# i=1
# while i<=rows:
#     j=i
#     while j<rows:
#         print(" ", end=" ")
#         j+=1
#     k=1
#     while k<=i:
#         print("*", end=" ")
#         k+=1
#     print()
#     i+=1                    

# rows=5
# i=rows
# while i>=0:
#     j=0
#     while j<i:
#         print("",end=" ")
#         j+=1
#     k=i
#     while k<=rows-1:
#         print(" *",end=" ")
#         k+=1
#     print()
#     i-=1
# i=0
# while i<=5-1:
#     j=0
#     while j<i:
#         print("",end=" ")
#         j+=1
#     k=i
#     while k<=rows-1:
#         print(" *",end=" ")
#         k+=1
#     print()
#     i+=1

# ** star **

# i=1
# l=4
# while i<=5:
#     print(" "*l+i*" *"+l*" ")
#     i=i+1
#     l-=1
# s=1
# n=4
# while n>0:
#     print(" "*s+n*" *"+s*" ")
#     n=n-1
#     s=s+1
