import PizzaClass
import UserClass

userinfo = UserClass.User

print("\n------------------Welcome to Papa JOJO's!------------------\n")
name = input("What is Your name?: ")
input("\nNice to meet you, " + name)
email = input("\nwhat is your email address?: ")
address = input("What is your adress?: ")
userinfo = UserClass.User(name, email, address)

print("\nWhat size Pizza would you like?")
print(" (1) - Small\n (2) - Medium\n (3) - Large\n (4) - Extra Large")

x = 0 

while x == 0: 

    userselection = input("\nPlease select an option: ")

    if userselection == "1":
        x = x + 1
        print("Small Pizza, Good choice!")
        Pizza = PizzaClass.SmallPizza()
        print("\nOne Pizza of this size is $" + str(Pizza.Price))

    elif userselection == '2':
        x = x + 1
        print("Medium Pizza, Good choice!")
        Pizza = PizzaClass.MediumPizza()
        print("\nOne Pizza of this size is $" + str(Pizza.Price))

    
    elif userselection == '3':
        x = x + 1
        print("Large Pizza, Good choice!")
        Pizza = PizzaClass.LargePizza()
        print("\nOne Pizza of this size is $" + str(Pizza.Price))


    elif userselection == '4':
        x = x + 1
        print("Extra Large Pizza, VEERRRYYYY Good choice!")
        Pizza = PizzaClass.XLargePizza()
        print("\nOne Pizza of this size is $" + str(Pizza.Price))


    else:
        x = 0
        print("Invalid input, try again.\n")

print("Discount: Buy 3 or more pizza's and get ~~ 15% OFF ~~ final price!\n")


a = 0 

while a == 0:
    userchoice2 = input("How many pizza's would you like? Please enter a digit: ")

    if int(userchoice2) > 0:
        a = a + 1
        print("You have ordered " + str(userchoice2) + " " + Pizza.name + "'s")
        
    else:
        x = 0
        print("Invalid input, try again.")

t = 0

while t == 0:
    if float(userchoice2) >= 3:
        print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - RECIPT - - - - - - - - - - - - - - - - - - - - - - -\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
        t = t + 1
        TotalPrice = round(((float(userchoice2) * float(Pizza.Price)) * 0.85), 2)
        print("Your total after discount is: $" + str(TotalPrice))
        print("Order will be delivered to: " + str(userinfo.name) + " at " + str(userinfo.address))
        print("Receipt will sent via email to: " + str(userinfo.email))
    
    else:
        print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - RECIPT - - - - - - - - - - - - - - - - - - - - - - -\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
        t = t + 1
        TotalPrice = round((float(userchoice2) * float(Pizza.Price)), 2)
        print("Your total is: $" + str(TotalPrice))
        print("Order will be delivered to: " + str(userinfo.name) + " at " + str(userinfo.address))
        print("Receipt will sent via email to: " + str(userinfo.email))