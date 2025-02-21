from math import ceil
from scipy.stats import binom
class FootballEvent:
    bet = 100
    def __init__(self, home, tie, away):
        self.home = home
        self.tie = tie
        self.away = away
        self.hprob = (1 / self.home)
        self.tprob = (1 / self.tie)
        self.aprob = (1 / self.away)

    def calculate_rake(self, *, explanation=False):
        rake = (self.hprob + self.tprob + self.aprob)-1
        if explanation == True:
            return f"The rake value of this event is {rake*100:.2f}%. "
        return rake

    def n_of_bets_for_profit(self, my_odd, place, *, confidence = 0.95, explanation = False):
        # Gets the booker odd based on "place". After that it calculates the minimum number of games you need to play,
        # based on your assessed probability "my_odd", by starting from 1 game and iterating win and game numbers,
        # but only for the condition that the combination of games played and wins achieved leads to a profit
        # (all other combinations are ignored). Returns only minimum games played and minimum number of wins.
        # Optionally you can print all the calculations up until the confidence point. Notice on the serial calculations
        # that the probability drops, especially at the start, when the algorithm changes the number of wins.
        # This is because it jumps to another binomial distribution.

        knet = self.bet_position_finder(place)
        i = 1
        oddprob = 1/my_odd
        while True:
            minWin = ceil(i/(knet+1))
            profit_p = 1 - binom.cdf(minWin-1, i, oddprob)
            actual_profit = self.bet*(minWin*(knet+1)-i)
            if explanation == True:
                print(f"{minWin}/{i} with p of this or more happening {profit_p:.2f} and total "
                      f"profit {actual_profit}€")
            if profit_p >= confidence:
                return i, minWin
            i += 1

    def bet_position_finder(self, place):
        match place:
            case "h":
                self.knet = self.home - 1
            case "t":
                self.knet = self.tie - 1
            case "a":
                self.knet = self.away - 1
            case _:
                raise ValueError("Invalid place. Please choose 'h' for home, 't' for tie, or 'a' for away.")
        return self.knet

    def set_games_profit_scenarios(self, my_odd, place, mockgames):
        # For a certain estimation of probability ""my_odd"" and a certain number of games "mockgames", prints
        # all the win scenarios, along with the respective profits and their probabilities. Also needs the "place"
        # variable to calculate the booker net profit offered based on his odds.
        knet = self.bet_position_finder(place)
        oddprob = 1 / my_odd
        game_list = []
        for mockwins in range(mockgames + 1):
            profit = (mockwins) * self.bet * (knet+1) - (mockgames) * self.bet
            pscenario = 1 - binom.cdf(mockwins - 1, mockgames, oddprob)
            game_list.append(f"{mockwins}/{mockgames} with profit {profit:.2f} and chance of that happening or "
                f"better {pscenario:.4f}")
            #print(
            #    f" {mockwins}/{mockgames} with profit {profit:.2f} and chance of that happening or "
            #    f"better {pscenario:.4f}")
        return game_list

    def estimated_wins_for_set_games(self, my_odd, mockgames, *, confidence = 0.95):
        oddprob = 1 / my_odd
        distance = (1 - confidence)/2
        # Calculate the confidence interval for the number of wins
        lower_bound = binom.ppf(distance, mockgames, oddprob)
        upper_bound = binom.ppf(1-distance, mockgames, oddprob)
        #print(f"Out of {mockgames} games, you will win between {lower_bound:.2f} and {upper_bound:.2f} "
        #      f"games with {confidence*100:.0f}% confidence.")
        return str(f"Out of <b>{mockgames}</b> games, you will win between <b>{lower_bound:.2f}</b> and <b>{upper_bound:.2f}</b> "
              f"games with <b>{confidence*100:.0f}%</b> confidence.")

    def __str__(self):
        rake = self.calculate_rake(explanation = False)
        return str(f"<div style='text-align: center;'><b style='font-size: 14px;'>1</b>: {self.home}"
                   f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                   f"<b style='font-size: 14px;'>X</b> : {self.tie}"
                   f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                   f"<b style='font-size: 14px;'>2</b>: {self.away}</div><br>"
                f"The booker estimates that the <u>Home Team</u> has a <b>{self.hprob * 100:.2f}%</b> chance of winning, "
                f"the <u>Tie</u> has a <b>{self.tprob * 100:.2f}%</b> chance of happening, and the <u>Away Team</u> has a "
                f"<b>{self.aprob * 100:.2f}%</b> chance of winning.<br>The above probabilities add up to "
                f"<b>{(rake + 1) * 100:.2f}%</b>, which means the rake is <b>{rake * 100:.2f}%</b>.")


if __name__ == "__main__":
    b = FootballEvent(4, 4, 2.5)
    #print(str(b))
    my_odd = 2.5
    my_oddchance = 1/my_odd
    place = "t"
    #Bet defined inside the class
    games, wins = b.n_of_bets_for_profit(my_odd, place, explanation=True)
    mockgames = 10
    print(games, wins)
    b.set_games_profit_scenarios(my_odd, place, mockgames)
    b.estimated_wins_for_set_games(my_odd, mockgames)


