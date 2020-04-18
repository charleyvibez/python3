from random import randint

def guessing_logic(no_guess, range_number):
    while no_guess > 0:
        computer_guess = randint(1, range_number)
        user_guess = input("Enter your guess: ")
        

        # checking if the user guess is alphabetic and not an integer
        if user_guess.isalpha():        
            print("Please input a valid number")

        # if it is not alphabetic running the else
        else:
            # if the user guess is correct
            if int(user_guess) == computer_guess:
                print("You guessed right")
            else:
                # if the user guess  is wrong
                no_guess-=1
                print(f"You guessed wrong!, the correct guess is {computer_guess}.\n You have {no_guess} guesses remaining ")
                4
                #condition when there is no number of guesses remaining
                if no_guess == 0:
                    print("Game over!")

while True:
    level = input("Choose your level of difficulty ('easy, medium, or hard'), to the end the game type 'end' \n- ").lower()

    # if level is easy
    if level == 'easy':
        guessing_logic(6,10)

    # if level is medium
    elif level == 'medium':
        guessing_logic(4, 20)

    # if level is hard
    elif level == 'hard':
        guessing_logic(3, 50)

    # To end Game
    elif level == 'end':
        print("Game ending.....")
        print("Gane ended!")
        break

    #Inavalid command inputted
    else:
        print("Invalid command")