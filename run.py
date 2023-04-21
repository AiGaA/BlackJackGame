import random

# The type of suit
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

# The type of card
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# The card value
cards_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}


def generate_deck():
    """
    Shuffles all cards in a deck
    """
    deck = []
    for suit in suits:
        for card in cards:
            deck.append((card, suit))
    random.shuffle(deck)
    return deck


def get_card_value(card):
    """
    Get card values
    """
    key = card[0]
    value = cards_values[key]
    return value


def turn(deck, current_score):
    """
    Returns card score
    """
    card = deck.pop(0)
    print(">> ", card)
    card_value = get_card_value(card)
    new_score = current_score + card_value
    print("Score: ", new_score)
    return new_score


def play_game():
    """
    Main block of code with all game functionality
    """
    deck = generate_deck()
    computer_score = 0
    player_score = 0
    print("-------------Computer Cards-------------")
    computer_score = turn(deck, computer_score)
    computer_score = turn(deck, computer_score)
    print("Computer score:", computer_score)

    print("-------------Players Cards-------------")
    player_score = turn(deck, player_score)
    player_score = turn(deck, player_score)
    print("Your score:", player_score)

    print("-------------Begin Game-------------")
    keep_playing = True
    while keep_playing:
        user_choice = input("HIT or STAND: ")
        if (user_choice == "HIT"):
            player_score = turn(deck, player_score)
            print("Your total:", player_score)
            print("Computer total:", computer_score)

            if player_score > 21:
                print("-------------You bust, computer wins!-------------")
                user_input = input("Would you like to repeat? Y/N\n")
                validate_input(user_input)

        elif (user_choice == "STAND"):
            print("-------------Computer Cards-------------")
            computer_score = turn(deck, computer_score)
            print("Your total:", player_score)
            print("Computer total:", computer_score)

            if computer_score > 21:
                print("-------------Computer busts, you win!-------------")
                user_input = input("Would you like to repeat? Y/N\n")
                validate_input(user_input)

            elif computer_score == player_score:
                print("-------------Tie!-------------")
                user_input = input("Would you like to repeat? Y/N\n")
                validate_input(user_input)

            elif computer_score > player_score:
                print("-------------You lose, computer wins!-------------")
                user_input = input("Would you like to repeat? Y/N\n")
                validate_input(user_input)

            else:
                print("-------------Computer loses, you win!-------------")
                user_input = input("Would you like to repeat? Y/N\n")
                validate_input(user_input)

        else:
            print("Please enter valid input: 'HIT' or 'STAND'")


def validate_input(repeat):
    """
    This block of code will validate if 'Y' or 'N' has been entered,
    game has ended and user get to choose to play again or end the game.
    """
    while True:
        if repeat == 'Y':
            main()
        elif repeat == 'N':
            print("Goodbye!")
            exit()
        else:
            print("Please enter 'Y' for yes or 'N' for no.")
            repeat = input("Would you like to repeat? Y/N\n")


def main():
    """
    Executes the main program
    """
    enter = input("           *** PRESS ENTER TO START ***              \n")
    if enter == '':  # hitting enter == '' empty string
        play_game()
    else:
        print("Exiting program.")
        exit()


print(" ___________________________________________________ ")
print("|          Welcome to the Black Jack game!          |")
print("|  The deck of cards is randomly generated for the  |")
print("|  player and the computer. To win the game, total  |")
print("|  score should be collected is 21. Whoever gets a  |")
print("|  score of 21 first is the winner!                 |")
print(" ___________________________________________________ ")

main()
