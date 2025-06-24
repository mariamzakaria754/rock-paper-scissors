import random  # Import the random module to allow random choices

# Function to get the user's choice
def get_user_choice():
    choice = input("Choose (rock, paper, scissors): ").strip().lower()  # Ask user for input and normalize it
    if choice not in ['rock', 'paper', 'scissors']:  # Validate input
        print("Invalid choice, please try again.")
        return get_user_choice()  # Retry if input is invalid
    return choice  # Return the valid choice

# Function to randomly choose for the computer
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])  # Random choice from the options

# Function to determine the winner of the round
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"  # Same choice = tie
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"  # Winning conditions for the user
    else:
        return "Computer wins!"  # Otherwise, computer wins

# Main game function
def play():
    print("Welcome to Rock, Paper, Scissors!")
    while True:  # Infinite loop to allow replaying
        user_choice = get_user_choice()  # Get user's choice
        computer_choice = get_computer_choice()  # Get computer's choice
        print(f"Your choice: {user_choice}")  # Show user's choice
        print(f"Computer's choice: {computer_choice}")  # Show computer's choice
        result = determine_winner(user_choice, computer_choice)  # Determine result
        print(result)  # Print the outcome

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")  # Exit message
            break  # Exit the loop and end the game

# Ensure the script runs the game only when executed directly
if __name__ == "__main__":
    play()
#______________________________________________________________________________________

    

# I WANT TO print the computer and player choise so the user can see what they choise

    import random

def play():
    print("Welcome to Rock, Paper, Scissors!")

    options = ['rock', 'paper', 'scissors']  # Available choices

    while True:
        # Get user input
        user_choice = input("Choose (rock, paper, scissors): ").strip().lower()

        # Validate input
        while user_choice not in options:
            print("Invalid choice, please try again.")
            user_choice = input("Choose (rock, paper, scissors): ").strip().lower()

        # Get computer choice
        computer_choice = random.choice(options)

        # Display both choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")

        # Determine winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("Computer wins!")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    play()

# can you make shorter as i see you repeated the condition of winning 3 times
import random

def play():
    # Welcome message for the user
    print("Welcome to Rock, Paper, Scissors!")

    # Game options
    options = ['rock', 'paper', 'scissors']
    # Winning cases for each choice
    winning_cases = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    while True:
        # Prompt the user to choose
        user_choice = input("Choose (rock, paper, scissors): ").strip().lower()

        # Check if the user's choice is valid
        while user_choice not in options:
            print("Invalid choice, please try again.")
            user_choice = input("Choose (rock, paper, scissors): ").strip().lower()

        # Computer randomly chooses
        computer_choice = random.choice(options)

        # Display both choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif winning_cases[user_choice] == computer_choice:
            print("You win!")
        else:
            print("Computer wins!")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

# Start the game
if __name__ == "__main__":
    play()


