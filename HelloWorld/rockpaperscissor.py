import random

user_wins = 0
com_wins = 0
draw = 0
options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type rock/paper/scissor or q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # 0=rock, 1=paper, 2=scissor
    com_pick = options[random_number]
    print("Computer picked: ", com_pick + ".")

    if user_input == "rock" and com_pick =="scissor":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and com_pick =="rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissor" and com_pick =="paper":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and com_pick =="paper":
        print("Draw!")
        draw += 1

    elif user_input == "scissor" and com_pick =="scissor":
        print("Draw!")
        draw += 1

    elif user_input == "rock" and com_pick == "rock":
        print("Draw!")
        draw += 1

    else:
        print("You lost!")
        com_wins += 1

print("==================")
print("You won ", user_wins, "times.")
print("Computer won ", com_wins, "times.")
print("And you drew ", draw, "times.")
print("Thank you for playing!")