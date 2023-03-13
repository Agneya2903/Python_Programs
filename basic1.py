#Python Program For Simple Interest
def simple_interest(p,r,t):
    print("The Principal Amount is", p,"Rs")
    print("The time period is",t, "years")
    print("The rate of interest is ",r,"%")

    si =(p*r*t/100)
    print("The Simple Interest for the given values is ",si)
    return si
simple_interest(3500,8.5,5)