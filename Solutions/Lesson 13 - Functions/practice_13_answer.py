"""
PROGRAM: Finance Helper Dashboard
This program helps to calulate different finacial values (discounts, gst)
"""

# =====================================================================
# FUNCTIONS
# =====================================================================

def calculate_discount():

    print("--- Tool 1: Discount Calculator ---")

    # Get price
    while True:
        price = input("What is the full price of the item? (number only)")
        try:
            price = float(price)
            break
        except:
            print("That's not a valid price")

    # Get discount
    while True:
        discount = input("What is the discount percentage? (number only)")
        try:
            discount = float(discount/100)
            break
        except:
            print("That's not a valid percentage")
    
    # Calculate and output cost
    print(f"The item will cost {price * (1-discount)}")


def calculate_gst():
    print("--- Tool 2: GST Calculator ---")

    # Get price
    while True:
        price = input("What is the price of the item? (number only)")
        try:
            price = float(price)
            break
        except:
            print("That's not a valid price")

    # Get gst included or excluded
    gst_included = input("Is GST included in the price?").lower() in ["y", "yes"]

    # Calculate gst
    if gst_included:
        gst = price * 3 / 23
        print(f"GST = ${gst}")
        print(f"Item without GST = ${price - gst}")
    else:
        gst = price * 0.15
        print(f"GST = ${gst}")
        print(f"Item with GST = ${price + gst}")


def main():

    print("📱 Welcome to the Finance Helper Dashboard 📱\n")
    print("1. Discount Calculator")
    print("2. GST Calculator")

    choice = input("\nWhich tool do you want to use? (1 or 2): ").strip()

    # Use logical operators to trigger the correct function
    if choice == "1":

        calculate_discount()
    
    elif choice == "2":
        
        calculate_gst()

    else:
        print("Invalid choice. Exiting dashboard.")



# =====================================================================
# MAIN EXECUTION
# =====================================================================

main()