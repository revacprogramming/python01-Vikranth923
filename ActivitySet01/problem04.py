hrs = input("Enter Hours:")
h = float(hrs)
r=float(input("enter rate"))
r2=1.5*r
if h<=40:
    print(h*r)
else:
    print(40*r+(h-40)*r2)