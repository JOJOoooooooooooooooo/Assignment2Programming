
#Creating the user class
class user:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

#Creating pizza class
class pizza: 
    def __init__(self,size, price, num):
        self.size = size
        self.price = price
        self.num = num

    def total (self):
        final = self.price * self.num

        #Coupon
        if self.num >= 3:
            final *= 0.85
        return final

    def str(self):
        return f"Pizza size: {self.size}, Price: $ {self.price}, Number of Pizzas: {self.num}"

#Getting user input
print("\n------------------Welcome to Papa Jojo's!------------------\n")
name = input("Enter your name: ")
email = input("Enter your email: ")
address = input("Enter your address: ")

#Assigning the user info
userinfo = user(name, email, address)

#Getting pizza input
print("\n\nHave a look at the sizes:")
x = 0

while x == 0:
    print("(1) - Small\n(2) - Medium\n(3) - Large\n(4) - X-Large")
    size = input("Enter the number to the corresponding pizza size desired: ")

    if size == "1" or "2" or "3" or "4":
        x = x + 1
    else:
        print("\nInvalid input, try agian.\n")

sizePrice = {"1": 10, "2": 12, "3": 15, "4": 18}

price = sizePrice[size]

num = int(input("Enter the number of Pizza's: "))

#Assigning the pizza info
order = pizza(size, price, num)

#Displaying the recipt
final = order.total()
print("\nReciept:")
print(f"\nCustomer name: {userinfo.name}")
print(f"Reciept sent to: {userinfo.email}")
print(f"Location to deliver: {userinfo.address}")
print(f"Order details: {order.str()}")
print(f"Final price(After tax and any availabe discounts): ${final:.2f}")