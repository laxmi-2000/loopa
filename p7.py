# *** guessing game ***
# a=int(input("enter the number"))
# i=1
# while i<=a:
#     if i==5:
#         print("is equal",i)
#     else:
#         print("it's not equal",i)
#     i=i+1


# *** guessing game ***

# num=5
# guess=int(input("enter the number 1 to 10:-"))
# while guess!=num:
#     print("your guess is incorrect plz try again ")
#     guess=int(input("enter the number 1 to 10:-"))
# print("congrats, your guess is correct")




i=1
b=0
while i<=5:
    b=int(input("enter the number:-"))
    if b==5:
        print("congrats,your guess is correct")
        print("its equal")
        break
    else:
        print("your guess is incorrect:-:")
        i=i+1

