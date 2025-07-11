def vending_machine():
    # Initialize the vending machine items
    items = {
        1: {"name": "Chips", "price": 1.50},
        2: {"name": "Chocolate Bar", "price": 1.25},
        3: {"name": "Pretzels", "price": 1.00},
        4: {"name": "Soda", "price": 1.75},
        5: {"name": "Water", "price": 1.00},
        6: {"name": "Gum", "price": 0.75},
        7: {"name": "Cookies", "price": 2.00},
        8: {"name": "Candy", "price": 1.50}
    }
    
    # Display welcome message
    print("Welcome to the Python Vending Machine!")
    print("Please select items by their number. Type 'done' when finished.\n")
    
    # Display available items
    print("Available Items:")
    print("----------------")
    for num, item in items.items():
        print(f"{num}. {item['name']} - ${item['price']:.2f}")
    print()
    
    # Initialize shopping cart
    cart = []
    total = 0.0
    
    # Main selection loop
    while True:
        selection = input("Enter item number (or 'done' to finish): ")
        
        if selection.lower() == 'done':
            break
            
        try:
            item_num = int(selection)
            if item_num in items:
                item = items[item_num]
                cart.append(item)
                total += item["price"]
                print(f"Added {item['name']} to your cart. Current total: ${total:.2f}")
            else:
                print("Invalid item number. Please try again.")
        except ValueError:
            print("Please enter a valid number or 'done'.")
    
    # Print receipt
    print("\nYour Receipt:")
    print("-------------")
    for item in cart:
        print(f"{item['name']}: ${item['price']:.2f}")
    
    print(f"\nTotal: ${total:.2f}")
    print("Thank you for using the Python Vending Machine!")

# Run the vending machine
vending_machine()