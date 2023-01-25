p = float(input("Enter the principal amount : "))
t = float(input("Enter the number of years : ")) 
r = float(input("Enter the rate of interest : "))

si = (p * t * r)/100
ci =  p * (pow((1 + r / 100), t)) 

print("Simple interest : {}".format(si))
print("Compound interest : {}".format(ci))