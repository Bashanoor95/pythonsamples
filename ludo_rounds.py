#player1, player2, player3
import random

# roll = [1,2,3,4,5,6]


def roll_dice():
    value = random.choice([1, 2, 3, 4, 5, 6])
    return value


def ludo(player_list):
    flag = 1
    # player_list = ["player1", "player2", "player3"]
    while player_list:
        for player in player_list:
            input(f"click enter to roll dice for {player}")
            num = roll_dice()
            print(f"you got {num}")
            if num == 6:
                print(f"{player} has won")
                player_list.remove(player)
            else:
                print("please try again")

    return "Thankyou for playing!!!"


if __name__ == "__main__":
    player_count = int(input("Enter the number of players: "))
    players = []
    for index in (range(1, player_count+1)):
        name_of_the_player = input(f"Enter the name of player {index}: ")
        players.append(name_of_the_player)

    ludo(player_list=players)
