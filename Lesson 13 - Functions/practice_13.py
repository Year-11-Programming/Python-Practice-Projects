"""
PROGRAM: Video Game Profile Setup
This program helps the user create a profile for a generic video game.
"""

# =====================================================================
# VALUES
# =====================================================================
character_name = ""
level = 1
has_bonus_health = False
can_enter_dungeon = True

# =====================================================================
# FUNCTIONS
# =====================================================================

# TODO Create a function for creating character. 
# TODO Copy and paste all the relevent code from below into new function.
# TODO Write a comment above the function to explain what it does
# TODO Replace the copied code below with a function call.


# TODO Create a function for showing status. 
# TODO Copy and paste all the relevent code from below into new function.
# TODO Write a comment above the function to explain what it does
# TODO Replace the copied code below with a function call.


# TODO Create a main function for running the program.
# TODO Copy and paste all remaining code (including your new calls) into this function.
# TODO Replace the copied code below with a main function call.


# =====================================================================
# MAIN EXECUTION
# =====================================================================

print("⚔️ Welcome to the RPG Character Creator ⚔️\n")

# Create character and stats
user_input = input("Enter your character's name: ")
character_name = user_input.strip().upper()

while True:
    level = input("Enter starting level (1-10): ")
    try:
        level = int(level)
        if level >= 1 and level <= 10:
            break
        else:
            print("That level doesn't exist.")
    except:
        print("That's not a number.")

is_ready = input("Is your character ready for battle? (yes/no): ").strip().lower() == "yes"

# Calculate special stats based on inputs
has_bonus_health = level > 5
can_enter_dungeon = is_ready and (level >= 3)

# Show current status
print("\n=== 📜 OFFICIAL CHARACTER SHEET 📜 ===")
print(f"NAME:         {character_name}")
print(f"STARTING LVL: {level}")
print(f"BONUS HP:     {has_bonus_health}")
print(f"DUNGEON PASS: {can_enter_dungeon}")
print("=====================================")