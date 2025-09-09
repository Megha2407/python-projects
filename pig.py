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

        

