fuel=float(input("Enter fuel echonomy (L): "))
dis=float(input("Enter total distance (Km): "))
hwy=float(input("Enter hightway charges (LKR): "))

fc=fuel*410

tot=fc + hwy

fe=dis/fuel
float(fe)
float(tot)
float(fc)

print("Fuel consumption ", fe ,"L/Km")
print("Total fuel cost ",fc , "LKR")
print("Total cost " , tot, "LKR")
