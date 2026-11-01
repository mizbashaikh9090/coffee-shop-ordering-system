# colour codes
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'
MAGENTA = '\033[35m'

greeting = "Welcome to Luxe Latte!"
print(f"{greeting:~^50}")

print("menu:- \n\n")

print("ID")
print("01 - Black Coffee: $3")
print("02 - Latte: $4")
print("03 - Frappuccino: $5")

total_price = 0
order_list = []
order = 0

while True:
    
    print("\n\n")
    
    order = input(GREEN + "What would you like to order? (type 'done' to finish ordering): " + RESET)
    
    order = order.strip().lower()
    
    if order == "01":
        total_price += 3
        order_list.append("Black Coffee: $3")
        print("Done!")
        
        
    elif order == "02":
        total_price += 4
        order_list.append("Latte: $4")
        print("Done!")
        
    elif order == "03":
        total_price += 5
        order_list.append("Frappuccino: $5")
        print("Done!")
        
    elif order == "done":
        break 
          
    else:
        print(f"{order} is not a valid order or is not available.")
    
print("\n\n")

extra = input(GREEN + "Would you like whipped cream in your order for an extra $1? (yes/no): " + RESET)
extra = extra.strip().lower()

if extra == "yes":
    total_price += 1
    order_list.append("Whipped Cream: $1")

elif extra == "no":
    pass
                 
else:
    print("Please type in either 'yes' or 'no' ")

print("\n\n")
                
print(MAGENTA + f"Your total bill is ${total_price:.2f}")
print("\n\n")
print("Here is the list of items you ordered:")
for item in order_list:
    print(item)
    
print("Thank you for ordering!" + RESET)                                                                                   
      
