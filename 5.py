sl=int(input("enter your salary "))
y=int(input('enter the year of of service'))
if y>5:
    b=(5/100)*sl
    a=sl+b
    print("The net bonus amount is" , a  )

else :
    print("not eligible for the bonus")
