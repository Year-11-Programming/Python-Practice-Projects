# Use this file to investigate different lines of code.
MULT_NUM = 5
INSTRUCTIONS = "Choose a number and I will multiply it by " + str(5)

name = input("Hi! What's your name?")
print("Hi", name)
print(INSTRUCTIONS)
num = input("What number should I multiply?")
print("The answer is:", int(num) * MULT_NUM)