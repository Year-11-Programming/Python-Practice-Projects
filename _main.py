import time

# Run a timer based on user input
def run_timer():
    # Ask the user how long they want to wait
    seconds_input = input("How many seconds do you want to set the timer for? ")
    seconds = int(seconds_input)
    
    print("Timer started...")
    
    # Pause the program for that many seconds
    time.sleep(seconds)

# Output the "alarm" message
def output_alarm():
    
    print("\n⏱️ BEEP BEEP BEEP!")
    print("Time's up! Your timer has finished.")
    print("---------------------------------")

def main():

    # Introduction
    print("Welcome to the Timer App")

    # Loop program
    while True:
        run_timer()
        output_alarm()
        user_input = input("Do you want to run another timer?")
        if not user_input.lower() in ["y", "yes", "ya", "yeah", "yep", "yup"]:
            break

if __name__ == "main":
    main()