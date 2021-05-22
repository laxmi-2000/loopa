  

# i=1
# g=0
# while i<=5:
#     guess=int(input("enter the number"))
#     if i<5:
#         print("try again,its low")
#     elif i>5:
#         print("try again, its high")
#     elif i==5:
#         print("congrats you have winer")
#     i=i+1


i=1
a=10
while i<=5:
    num=int(input("enter the number"))
    if num==a:
        print("congrats,you have winer")
        break
    elif num<a:
        print("your gessing is low")
    else:
        print("your gessing is high")
    i=i+1