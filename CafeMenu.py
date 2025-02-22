menu = {
    'coffee': 80,
    'Pizza':150,
    'Burger':90,
    'Hot choclate':150,
}
bill=0
print("hello sir WECLOME TO CAFE.PY \n how are you?, this is our Menu coffee': Coffie \n Pizza \n Burger \n Hot choclate"
    )
item_1= input("what you would like to order:") 
if(item_1 in menu):
    bill += menu[item_1]
    print("your Item {item_1} is added")
else:print("It is not available")

another_order = input("would you like to add something more:(yes/no)")

if another_order == "yes":
    item_2 = input("What would you like to add: ") 

    if item_2 in menu:  # Check if item is available
        bill += menu[item_2]  # Add item price to bill
        print(f"Your item {item_2} is added.")
    else:
        print("It is not available.")

print(f"Sir, your bill is {bill}") 




