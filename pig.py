import random 

def roll():
    min_value = 1
    max_value = 6
    roll= random.randint(min_value,max_value)

    return roll
while True:
    players = input("Enter number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <=4:
            break
        else:
            print("must be btw the 2<= and <=4")
    else:
        print("Invaild,try again")
        
max_score = 50
players_score =[0 for _ in range(players)]

while max(players_score) < max_score:
     for player_indx in range(players):
        current_score = 0
        
        while True:
            should_roll = input("would you like to roll? (y/n): ")
            if should_roll.lower()!= "y":
                break
            value = roll()
            if value == 1:
                print("you rolled a 1, your turn is over")
                break
            else:
                current_score += value
                print("you rolled a", value)
            print("your current score is", current_score)
        players_score[player_indx] += current_score
        print("player", player_indx + 1, "your total score is", players_score[player_indx])
    

















