age =int(input("enetr your age "))
t=1000
if age>=6 and age<14:
    print ("free")
elif age>14 and age<=25:
    amount=t - (50/100)*t 
    print("ticket price is ", amount)
elif age>25 and age<=36:
    amount=t -(20/100)*t 
    print("ticket price is ", amount)
else :
    amount=t-(10/100)*t
    print("ticket price is", amount)