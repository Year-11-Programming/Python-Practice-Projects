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

# Creates a charcter and its stats
def create_character():

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


# Outputs all the stats for character
def show_status():

    print("\n=== 📜 OFFICIAL CHARACTER SHEET 📜 ===")
    print(f"NAME:         {character_name}")
    print(f"STARTING LVL: {level}")
    print(f"BONUS HP:     {has_bonus_health}")
    print(f"DUNGEON PASS: {can_enter_dungeon}")
    print("=====================================")


def main():

    # Introduction
    print("⚔️ Welcome to the RPG Character Creator ⚔️\n")

    create_character()
    show_status()


# =====================================================================
# MAIN EXECUTION
# =====================================================================

main()