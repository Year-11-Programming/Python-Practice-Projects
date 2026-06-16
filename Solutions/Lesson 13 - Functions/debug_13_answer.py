"""
PROGRAM: Smart Home Security
This sets alarm sound and sounds the alarm when door is unlocked.
"""

#============================================
# VALUES
#============================================

security_status = "LOCKED"
global alarm_sound = "SIREN"

#============================================
# FUNCTIONS
#============================================

# Sets off the alarm
def trigger_alarm():
    print(f"Alert! Sounding the {alarm_sound}")


# Checks the system and secruity status, and sounds the alarm if it's not locked
def check_system():
    print("Checking home network stability...")
    if security_status == "LOCKED":
        print("All doors are secured.")
    else:
        trigger_alarm()


# resets the system to original state
def reset_system():
    print("System rebooting...")


# Runs the main program
def main():
    print(f"The current alarm sound is: {alarm_sound}")
    check_system()
    reset_system()

#============================================
# EXECUTION
#============================================

main()