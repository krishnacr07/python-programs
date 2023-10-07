per=int(input("enter the percentage"))
if per>=70 :
    print("First Division")
elif per<70 and per>=50:
    print("Second Division")
elif per<50 and per<=35:
    print("Third Division")
else:
    print("Fail")