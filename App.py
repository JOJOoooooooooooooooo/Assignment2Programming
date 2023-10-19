import PizzaClass



print("What size Pizza would you like?")
input("1: Small, 2: Medium, 3: Large or 4: Extra Large")


userselection = input("Please select an option: ")

x = 0 

while x == 0: 

    if userselection == "1":
        x += 1
        print("Small Pizza, Good choice!")
        Pizza = PizzaClass.SmallPizza

    elif userselection == '2':
        x += 1
        print("Medium Pizza, Good choice!")
        Pizza = PizzaClass.MediumPizza
    
    elif userselection == '3':
        x += 1
        print("Large Pizza, Good choice!")
        Pizza = PizzaClass.LargePizza

    elif userselection == '4':
        x =+ 1
        print("Extra Large Pizza, Good choice!")
        Pizza = PizzaClass.XLargePizza

    else:
        print("Invalid input")