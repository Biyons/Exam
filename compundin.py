def compound_interest(a,b,c):
    ta=a*(1+r/100)**n
    ai=ta-p
    print("Compound interest=",ai)
p=int(input("Enter principal amount:"))
r=float(input("Enter rate of interest:"))
n=int(input("Enter the number of years:"))
x=compound_interest(p,r,n)