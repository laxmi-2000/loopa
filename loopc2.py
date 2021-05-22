# Ek program banao jo 1 se 100 tak ke numbers ke saath yeh kare: 
# 1. Jo 3 se divisible hain unki jagah "Nav" print kare 2. Jo 7 
# se divisible hain unki jagah "Gurukul" print kare 3. Jo 3 aur 
# 7 dono se divisible hain,unki jagah "NavGurukul" print karein 
# 4. Jo upar wale teen cases mein nahi aate, unki jagah sirf number 
# print karvao.

i=1
while i<=100:
    if i%3==0 and i%7==0:
        print("navgurukul")
    elif i%3==0:
        print("nav")
    elif i%7==0:
        print("gurukul")  
    else:
        print(i)  
    i=i+1      

# # **** chocolate ****
# i=1
# while i<=100:
#     if i%5==0 and i%9==0:
#         print("Chocolate")
#     elif i%5==0:
#         print("Choco")
#     elif i%9==0:
#         print("late")
#     else:
#         print(i)
#     i=i+1

# i=1
# while i<=50:
#     if i%2==0 and i%3==0:
#         print("Ringo-Bingo")
#     elif i%2==0:
#         print("Ringo")
#     elif i%3==0:
#         print("Bingo")
#     else:
#         print("navgurukl")
#     i=i+1

# i=1
# while i<=200:
#     if (i%2==0 or i<=100) and (i%5==0 or i>=100):
#         print(i,"Ringo-Bingo")
#     elif i%2==0 or i<=100:
#         print(i,"Ringo")
#     elif i%5==0 or i>=100:
#         print(i,"Bingo")
#     i=i+1
        




