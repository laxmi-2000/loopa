# 11 logon ka weight input le aur fir average weight print kare. Aur fir yeh bhi 
# check kare ki kya Average weight 5 ka multiple (Yaani 5 se bhaag karne par 
# shesh 0 bachta hai) hai ya nahi? Note: Isme aapko input ka use karna padega.
#  Aap loop ke andar raw input ka use kar ke 11 baar raw_input le sakte ho.
        
# weight=int(input("enter the weight:-"))
# i=1
# sum=0
# while i<=11:
#     weight=int(input("enter the waight"))
#     if i%5==0:
#         # sum=sum+1
#         print(sum)
#     i=i+1

i=1
sum=0
while i<=11:
    waight=int(input("enter the number:-"))
    sum=sum+waight
    average=sum/11
    i=i+1
print(average)
if average%5==0:
    print("it is divisiable",average)
else:
    print("it is not divisiable",average)
