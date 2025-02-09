from utils.function_base import FootballEvent
import sys

def odds_validation(place):
    isRunning = True
    while isRunning:
        try:
            odd = float(input(f"{place} odds: "))
            if odd>1 and odd<=1000:
                isRunning = False
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 1000.")
    return odd
def my_odd_validation():
    isRunning = True
    while isRunning:
        try:
            my_odd = float(input(f"Your odd: "))
            if my_odd>1 and my_odd<=1000:
                isRunning = False
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 1000.")
    isRunning = True
    while isRunning:
        try:
            my_place = str(input(f"Where do you bet? (Home, Tie, Away): "))
            if my_place[0].lower() == "h" or my_place[0].lower() == "t".lower() or my_place[0].lower() == "a".lower():
                isRunning = False
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. You can only enter (Home, Tie, Away)")
    if my_place[0].lower() == "h":
        validator = home
        validator_option = "Home"
    elif my_place[0].lower() == "t":
        validator = tie
        validator_option = "Tie"
    elif my_place[0].lower() == "a":
        validator = away
        validator_option = "Away"
    if validator > my_odd:
        print(f"Your odd is {my_odd} and the booker's odd is {validator} for {validator_option}.")
        return my_odd, my_place[0].lower(), validator_option
    else:
        print(f"Your odd is {my_odd} and the booker's odd is {validator} for {validator_option}. \nNo luck in this "
              f"betting option! Try something else:")
        return my_odd_validation()

def function_choice():
    isRunning = True
    while isRunning:
        try:
            choice = int(input(f"You now have the options below:\n1. Calculate the minimum number of games you need"
                               f" to play\n2. Get all profit scenarios and cumulative probabilites for a set number "
                               f"of games played\n3. Get a range of expected wins for a given number of played "
                               f"games\n: "))
            if choice in range(1, 4):
                isRunning = False
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please choose 1,2 or 3:")
    return choice

if __name__ == "__main__":

    print("Welcome to BookEnemy \n...Initializing the event ...\n"
          "Please insert the odds of your event (Home, Tie, Away)")
    home = odds_validation("Home")
    tie = odds_validation("Tie")
    away = odds_validation("Away")
    b = FootballEvent(home, tie, away)
    print("###Event initialized!###\n"+str(b))
    print("What is your estimated true odd for any of the betting options?: ")
    my_odd, my_place, my_place_option = my_odd_validation()
    isRunning = True
    while isRunning:
        choice = function_choice()
        if choice == 1:
            games, wins = b.n_of_bets_for_profit(my_odd, my_place)
            print(f"To get profit with a confidence of 95% for a {my_odd} odd on the {my_place_option} option, "
                  f"you need to play at least {games} similar games. In these games, you'll win at "
                  f"least {wins} with a confidence of at least 95% ")
        elif choice == 2:
            mockgames = int(input("How many games do you want to simulate?: "))
            b.set_games_profit_scenarios(my_odd, my_place, mockgames)
        elif choice == 3:
            mockgames = int(input("How many games do you want to simulate?: "))
            b.estimated_wins_for_set_games(my_odd, mockgames)
        checker = str(input("Enter 'E' to exit the program or any other key to go back to the menu: "))
        if checker.lower() == "e":
            isRunning = False
            sys.exit("Shutting down...")



