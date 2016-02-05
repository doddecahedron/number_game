import random

def game():
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
        try:
            guess = int(input("Guess a number between 1 and 10: "))

            if guess == secret_num:
                print("You got it: My number was {}".format(secret_num))
                break
            elif guess < secret_num:
                print("My number is higher than {}".format(guess))
            else:
                print("My number is lower than {}".format(guess))
            guesses.append(guess)
        except ValueError:
            print("That's not a number! ")

    else:
        print("You didn't get it! My number was {}".format(secret_num))

    play_again = input("Do you want to play again? Y/n ")
    if play_again.lower() == 'Y':
        game()
    else:
        print("Deuces Homie!")

game()