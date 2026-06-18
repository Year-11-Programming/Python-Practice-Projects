"""
PROGRAM: Game Shop
This program runs a shop that displays user and shop inventory, can buy and sell items and displays gold.
"""

# INSTRUCTIONS
# Create functions for:
    # Displaying items
    # buy/sell function
# Display the shop menu (in main()): Buy, Sell, Exit (Give user choice and call functions based on this)



#===============================
# CONSTANTS
#===============================

# TODO Create constant for item_price and set to 20 
# (all items will cost the same - you can change this by using dictionaries for items instead)

#===============================
# FUNCTIONS
#===============================

# Display items with prices
# TODO Create function called display_items with parameters: items, action
    # TODO Loop through the items
        # TODO Print the item name and item_price
    
    # TODO Create an infinite while loop
        # TODO Ask the user which item they'd like to (action)

        # TODO If input is 'EXIT'
            # TODO return

        # TODO Loop through the items list
            # TODO Check if the input equals the item
                # TODO If it does, check if action is 'buy'
                    #TODO return item

        # TODO Output that that is not an available item


# Run main code
# TODO Create main function
    # TODO Create a list of shop items (each item can be a list or dictionary showing name and price)
    # TODO Create an empty list of inventory items
    # TODO Create a gold variable and set it to 500

    # TODO Welcome the player to the shop

    # TODO Create an infinite while loop
        # TODO Ask if they want to buy or sell

        # TODO If input is 'EXIT'
            # TODO break

        # TODO Check if input is buy
            # TODO run the display_items function (passing shop_items and 'buy') and save the return value in variable called item
            # TODO Check if item is not None
                # TODO Add item to inventory
                # TODO Remove item from shop
                # TODO Minus item_price from gold and resave in variable

        # TODO Check if input is sell
            # TODO run the display_items function (passing inventory and 'sell') and save the return value in variable called item
            # TODO Check if item is not None
                # TODO Add item to shop
                # TODO Remove item from inventory
                # TODO Add item_price to gold and resave in variable

        # TODO Otherwise tell them that's not valid input
    
    # TODO Tell the user goodbye.

        


#===============================
# EXECUTION
#===============================

# Execute main code



#===============================
#===============================
# EXTENSION
# Create dictionaries for each item for flexibility and to display other info: attack, defence, item_description
