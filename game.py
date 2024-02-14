import random

def main():
    # Generate a random winning number between 1 and 100
    winning_number = random.randint(1, 100)

    while True:
        try:
            # Prompt the user to enter their guess
            guess_number = int(input("Enter your guess (a number between 1 and 100): "))

            # Check if the guess is valid (between 1 and 100)
            if 1 <= guess_number <= 100:
                if guess_number == winning_number:
                    print("You win!")
                    break  # Exit the loop if the guess is correct
                elif guess_number < winning_number:
                    print("Too low")
                else:
                    print("Too high")
            else:
                print("Invalid input! Please enter a number between 1 and 100.")

            # Ask the user if they want to continue playing
            play_again = input("Do you want to continue playing? (yes/no): ").lower()
            if play_again != 'yes':
                print(f"The winning number was {winning_number}. Thanks for playing!")
                break  # Exit the loop if the user doesn't want to play again

        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Call the main function to start the game
main()
