import random

def play_game():
    random_num = random.randint(1, 100)
    chances = 0

    print("1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")
    level = input("Please select the difficulty level: ")

    if level == "1":
        chances = 10
        print("Great! You have selected the Easy difficulty level.")
    elif level == "2":
        chances = 5
        print("Great! You have selected the Medium difficulty level.")
    elif level == "3":
        chances = 3
        print("Great! You have selected the Hard difficulty level.")

    while chances > 0:
        user_choice = int(input("Enter your choice: "))

        if user_choice == random_num:
            attempts = 10 - chances + 1
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            return True

        chances -= 1
        if random_num > user_choice:
            print(f"Incorrect! The number is greater than {user_choice}.")
        elif random_num < user_choice:
            print(f"Incorrect! The number is less than {user_choice}.")

        if chances > 0:
            print(f"Chances remaining: {chances}")

    print("You have run out of chances. Try better next time.")
    return False

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

play_again = True
while play_again:
    play_game()
    another_try = input("Do you want to play again? (Y/N): ").lower()
    if another_try != "y":
        play_again = False
    



        
