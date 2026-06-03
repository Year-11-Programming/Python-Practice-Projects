banned_items = ["slingshot","laser"]
inventory = ["apple","slingshot","book","laser"]
confiscated = []
print(f"Scanning inventory: (inventory)")
for item in inventory
if item in banned_items:
print(f"Alert! Found banned item: {inventory[0]}")
confiscated.append(item)
inventory.pop(item)
print(f"Scan complete. Total flag matches: {len(banned_items)}")
if len(confiscated) > 0:
    print("Items confiscated:")
    # FOR the number of items in the confiscated list (use index)
        # PRINT the item listed with a number (eg. 1. Laser)