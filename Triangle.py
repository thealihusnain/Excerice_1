# Find the Area of Triangle
while True:
    # Take the base of Triangle from user
    Base = int(input("Enter the Base of Triangle :"))
    if(Base == 0):
       break
    # Take the Height of the Triangle from user
    Height = int(input("Enter the heigh of Triangle :"))
    # By use formula of triangle 
    Trianlge = 0.5*Base*Height
    # Disply the Triangle 
    print("Triangle of the Area is :",Trianlge)
