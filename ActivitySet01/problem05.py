def computepay(h, r):
    r2 = 1.5*r
    if hrs<=40:
        return hrs*p
    else:
        return (40*r +(hrs-40)*r2)
    

hrs = float(input("Enter Hours:"))
r = float(input("rate"))
p = computepay(hrs,r)
print("Pay", p)