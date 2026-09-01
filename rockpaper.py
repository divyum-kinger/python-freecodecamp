import random


def get_choices():
    player_choice = input("Enter a choice(rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

# def check_win(player, computer):
#     player =
#     print(f"you chose {player}, computer cho-se {computer}")
#     if player==computer:
#         return "its a tie"
#     elif player=="rock" and computer=="paper" or player=="paper" and computer=="scissors" or player=="scissors" and computer=="rock":
#         return "lose"
#     else:
#         return "win"
#

def check_win(player: str, computer: str):
    print(f"you chose {player}, computer cho-se {computer}")
    if player==computer:
        return "its a tie"
    elif player == "rock":
        if computer == "paper":
            return "rock covers paper. u win"
        else:
            return "rock breaks scissors. u lose"
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock u win"
        else:
            return "scissors cut paper u lose"
    elif player=="scissors":
        if computer=="paper":
            return "scissors cut paper u win"
        else:
            return "rock break scissors u lose"

choices = get_choices()
p_choice = choices["player"]
c_choice = choices["computer"]
print(check_win(p_choice, c_choice))

# choices = get_choices()
# print(choices)

# food = ["pizza", "carrots", "eggs"]
# dinner = random.choice(food)
# print(dinner)
