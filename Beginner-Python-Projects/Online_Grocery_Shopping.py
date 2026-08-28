#This program replicates the process of online grocery shopping applications using Python.


# Sample lists of items in aisles
produce_aisle = ['Apples', 'Bananas', 'Carrots', 'Lettuce', 'Spinach', 'Tomatoes', 'Potatoes', 'Broccoli', 'Oranges',
                 'Strawberries']
meats_aisle = ['Chicken Breast', 'Chicken Thighs', 'Chicken Drumsticks', 'Chicken Wings', 'Beef Sirloin', 'Beef Ribeye',
               'Beef Ground', 'Beef Brisket', 'Beef Tenderloin', 'Beef Flank Steak']
seafood_aisle = ['Lobster', 'Tilapia', 'Salmon', 'Cod', 'Shrimp', 'Oysters']
snacks_aisle = ['Potato Chips', 'Milk Chocolate', 'Gummy Bears', 'Carbonated Water', 'Orange Juice', 'Apple Juice',
                'Chocolate Cookies', 'Muffins']

# Shopping Cart to hold user's selected items
shopping_cart = []


# Function to display available aisles and items (remove sold-out items)
def display_aisles():
    print("Welcome to the grocery store!")
    print("\nAisles Available:")
    print("1. Produce Aisle:", ', '.join(produce_aisle) if produce_aisle else "No items available")
    print("2. Meats Aisle:", ', '.join(meats_aisle) if meats_aisle else "No items available")
    print("3. Seafood Aisle:", ', '.join(seafood_aisle) if seafood_aisle else "No items available")
    print("4. Snacks Aisle:", ', '.join(snacks_aisle) if snacks_aisle else "No items available")
    print("5. View Cart")
    print("6. Exit\n")


# Function to add items to the cart (and remove from aisle)
def add_to_cart(aisle, aisle_name):
    print(f"Available items in {aisle_name}: {', '.join(aisle) if aisle else 'No items available'}")
    item = input(f"Enter the item to add from {aisle_name} aisle: ").capitalize()
    if item in aisle:
        shopping_cart.append(item)
        aisle.remove(item)  # Remove item from aisle after adding to cart
        print(f"{item} has been added to your cart.")
    else:
        print("Invalid item or item out of stock. Please try again.")


# Function to remove items from the cart
def remove_from_cart():
    item = input("Enter the item to remove from your cart: ").capitalize()
    if item in shopping_cart:
        shopping_cart.remove(item)
        print(f"{item} has been removed from your cart.")
    else:
        print("Item not found in your cart.")


# Function to view the current shopping cart
def view_cart():
    if shopping_cart:
        print("\nYour shopping cart contains:")
        for item in shopping_cart:
            print(f"- {item}")
    else:
        print("\nYour shopping cart is empty.")


# Main program loop
def shopping_program():
    while True:
        display_aisles()
        choice = input("Select an option: ")

        if choice == '1':
            add_to_cart(produce_aisle, "Produce")
        elif choice == '2':
            add_to_cart(meats_aisle, "Meats")
        elif choice == '3':
            add_to_cart(seafood_aisle, "Seafood")
        elif choice == '4':
            add_to_cart(snacks_aisle, "Snacks")
        elif choice == '5':
            view_cart()
        elif choice == '6':
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid option. Please try again.")

        # After every operation, let the user choose to add or remove items
        update_choice = input("\nWould you like to update your cart? (yes/no): ").strip().lower()
        if update_choice == "no":
            print("Thank you for using the shopping cart program!")
            break
        elif update_choice == "yes":
            cart_update_choice = input(
                "\nWould you like to (a) Add or (b) Remove items from your cart? (a/b): ").strip().lower()
            if cart_update_choice == 'a':
                item_aisle_choice = input(
                    "Which aisle would you like to add from? (Produce/Meats/Seafood/Snacks): ").strip().capitalize()
                if item_aisle_choice == 'Produce':
                    add_to_cart(produce_aisle, "Produce")
                elif item_aisle_choice == 'Meats':
                    add_to_cart(meats_aisle, "Meats")
                elif item_aisle_choice == 'Seafood':
                    add_to_cart(seafood_aisle, "Seafood")
                elif item_aisle_choice == 'Snacks':
                    add_to_cart(snacks_aisle, "Snacks")
                else:
                    print("Invalid aisle.")
            elif cart_update_choice == 'b':
                remove_from_cart()
            else:
                print("Invalid choice, returning to main menu.")
        else:
            print("Invalid input, returning to main menu.")


# Run the shopping program
shopping_program()
