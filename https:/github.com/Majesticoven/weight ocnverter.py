#weight converter
#convert from lbs to kg
#enter in kg or lbs
w=int(input("Weight"))
c=input("Lbs or Kg")
if c.lower() == "l":
    print("You are",w*0.45,"kg")
elif c.lower() == "k":
    print("You are",w/0.45,"lbs")
else:
    print("ERROR IN INPUT")
