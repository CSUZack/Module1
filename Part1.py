#recursive function to ask for a valid integer and to ask for a retry on any value error
def InputValidInt(prompt, retries=5):
    if retries <= 0:
        print("Too many failures in user input, aborting.\n")
        exit()
    try:
        return int(input(prompt))
    except ValueError:
        print("Something was wrong with that input, please try again.\n")
        retries -=1
        return InputValidInt(prompt, retries)
    
num1 = InputValidInt("Please type your first number and then press enter.\n")
num2 = InputValidInt("Please type your second number and then press enter.\n")

print("\nResults:\n")
print(f"{num1} + {num2} = {num1+num2}\n")
print(f"{num1} - {num2} = {num1-num2}\n")
print("Thanks for using my program.\n")