# **** prime number ****

i=1
while i<=100:
    if i%1==0 and i%2!=0:
        print("it is prime:",i)
    else:
        print("it's not prime:",i)
    i=i+1

# i=1
# while i<=100:
#     if i%2==0:
#         print(i,"even number")
#     else:
#         print(i,"odd number")
#     i=i+1