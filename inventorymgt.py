def inventory_management():
    inventory = {
        "Laptop": 10,
        "Mouse": 50,    
        "Keyboard": 30,
        "Monitor": 15
    }

    while True:
        print("\n--- Inventory Management System ---")
        print("1. Display Inventory")
        print("2. Add/Update Stock")
        print("3. Remove Item")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("\n--- Current Inventory ---")
            if not inventory:
                print("Inventory is empty.")
            else:
                # Loop to display each item and its quantity
                for item, quantity in inventory.items():
                    print(f"{item}: {quantity}")
        
        elif choice == '2':
            item_name = input("Enter item name to add/update: ").strip().title()
            while True:
                try:
                    quantity_str = input(f"Enter quantity for {item_name} (e.g., 5, -2 for removal): ")
                    quantity = int(quantity_str)
                    break
                except ValueError:
                    print("Invalid quantity. Please enter a whole number.")
            
            if item_name in inventory:
                inventory[item_name] += quantity
                if inventory[item_name] < 0:
                    print(f"Warning: Quantity for {item_name} is now negative ({inventory[item_name]}).")
                print(f"Updated {item_name}. New quantity: {inventory[item_name]}")
            else:
                if quantity >= 0:
                    inventory[item_name] = quantity
                    print(f"Added {item_name} with quantity: {quantity}")
                else:
                    print("Cannot add a new item with a negative quantity. Please enter a non-negative quantity.")

        elif choice == '3':
            item_name = input("Enter item name to remove: ").strip().title()
            if item_name in inventory:
                del inventory[item_name]
                print(f"{item_name} removed from inventory.")
            else:
                print(f"{item_name} not found in inventory.")

        elif choice == '4':
            print("Exiting Inventory Management System. Goodbye!")
            break  
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


inventory_management()