STEPS_IN_KM = 1312
GOAL = 5.0
USER_NAME = input("Enter athlete name: ")  
steps = input("How many steps did you walk? ")  
km_walked = steps / STEPS_IN_KM
km_rounded = round(km_walked, 2) 
print(user_name + " walked " + km_rounded + " km.")
goal_reached = km_rounded >= GOAL
print("Daily 5km Goal Met:")
print(km_rounded)