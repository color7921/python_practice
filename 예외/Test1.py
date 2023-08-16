try:
    user_input = input("Enter a number: ")
    number = int(user_input)
except ValueError:
    print("Invalid input. Please enter a valid number.")
