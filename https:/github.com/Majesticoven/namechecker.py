name=input("What is your name?(name must be between 3 and 50 charecters long)")
if len(name)< 3:
    print("Name must be more than 3 charecter long")
elif len(name)>50:    
        print("Nane must by less than 50 charecters long")
else:
    print("name looks good")
