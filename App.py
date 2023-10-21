import PizzaClass
import UserClass

userinfo = UserClass.User

print("What is Your name?")
name = input(": ")
print("Nice to meet you, " + name)
print("what is your email address?")
email = input(": ")
print("What is your adress?")
address = input(": ")
userinfo = UserClass.User(name, email, address)

print("What size Pizza would you like?")
input("1: Small, 2: Medium, 3: Large or 4: Extra Large")

x = 0 

while x == 0: 

    userselection = input("Please select an option: ")

    if userselection == "1":
        x = x + 1
        print("Small Pizza, Good choice!")
        Pizza = PizzaClass.SmallPizza()
        print("One Pizza of this size is $" + str(Pizza.Price))

    elif userselection == '2':
        x = x + 1
        print("Medium Pizza, Good choice!")
        Pizza = PizzaClass.MediumPizza()
        print("One Pizza of this size is $" + str(Pizza.Price))

    
    elif userselection == '3':
        x = x + 1
        print("Large Pizza, Good choice!")
        Pizza = PizzaClass.LargePizza()
        print("One Pizza of this size is $" + str(Pizza.Price))


    elif userselection == '4':
        x = x + 1
        print("Extra Large Pizza, Good choice!")
        Pizza = PizzaClass.XLargePizza()
        print("One Pizza of this size is $" + str(Pizza.Price))


    else:
        x = 0
        print("Invalid input")

print("how many Pizzas of this size would you like to order?")
print("please keep in mind, if you order 3 or more pizza's you get a 15 percent discount!")


a = 0 

while a == 0:
    userchoice2 = int(input(":"))

    if int(userchoice2) > 0:
        a = a + 1
        print("you have ordered " + str(userchoice2) + " " + Pizza.name + "'s")
        
    else:
        x = 0
        print("Invalid input")

t = 0

while t == 0:
    if int(userchoice2) >= 3:
        t = t + 1
        TotalPrice = (userchoice2 * Pizza.Price) * 0.85
        print("Your total after discount is, $" + str(TotalPrice))
        print("Order will be delivered to, " + str(userinfo.name) + " at " + str(userinfo.address))
        print("Receipt will be emailed to you via " + str(userinfo.email))
    
    else:
        t = t + 1
        TotalPrice = (userchoice2 * Pizza.Price)
        print("Your total is, $" + str(TotalPrice))
        print("Order will be delivered to, " + str(userinfo.name) + " at " + str(userinfo.address))
        print("Receipt will be emailed to you via " + str(userinfo.email))
    