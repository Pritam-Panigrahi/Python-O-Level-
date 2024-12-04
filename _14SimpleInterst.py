p = float(input("Enter Principle Amount:- "))
r = float(input("Enter Rate Of Interest :- "))
t = float(input("Enter Time :- "))

si = (p*r*t)/100
totalAmount = p+si
print("-"*20) #For Printing 20 Times "-"
print("Interst = ",si)
print("Total Amount = ",totalAmount)
print("-"*20)