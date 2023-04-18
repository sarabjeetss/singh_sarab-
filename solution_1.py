#  empty shopping cart as in assignment shows
 
shoppingCart = {}

# display the  menu as in assignment shows
print("WELCOME TO THE AMANDO SHOPPING SITE\n")
print("A. Add product to the cart.")
print("B. Search the product.")
print("C. Delete the product from the cart.")
print("D. Quit.")

# process the user input
while True:
    choice = input("\nEnter your choice: ")
    
    # add product to the cart
    if choice == "1":
        numItems = int(input("Enter the number of items to be added in the stationary shop: "))
        
        if len(shoppingCart) + numItems > 5:      #using function
            print("Cart is full")
        else:
            for i in range(numItems):
                item = input("Enter an item: ")
                brand = input("Enter the brand Name: ")
                shoppingCart[item] = brand
            
            print("You added following items to the cart:")
            for item, brand in shoppingCart.items():
                print(item + " : " + brand)
    
    # search product in cart
    elif choice == "2":
        item = input("Enter the item to be searched: ")
        
        if item in shoppingCart:
            print(item + " : " + shoppingCart[item])
        else:
            print("No product exists with this name")
    
    # delete product from  the cart
    elif choice == "3":
        if not shoppingCart:
            print("Cart is empty, no item is found")
        else:
            item = input("Enter the item to be deleted: ")
            
            if item in shoppingCart:
                del shoppingCart[item]
                print(item + " deleted from cart")
            else:
                print("No product exists with this name")
    
    # quit the program
    elif choice == "4":
        break
    
    # invalid the input
    else:
        print("Wrong Option Entered")
