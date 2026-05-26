import random
MAX_ATTEMPTS = 3
attempts = 0
system_status = "OFFLINE"
while attempts < MAX_ATTEMPTS and system_status == "OFFLINE":
boot_code = input("Enter boot code (START): ")
if boot_code.upper().strip() == "START":
print("System booting...")
system_status = "ONLINE"
else:
print("Invalid boot code.")
rand_num = randint(1,10)
if rand_num == 5:
print("Something went wrong")
else:
print("System online.")

#========================================
# EXTENSION
# TODO Add a 'magic eight ball' program for once the system is booted
# TODO Get the user to ask a yes/no question
# TODO Randomise a number and use that number to give them a reponse