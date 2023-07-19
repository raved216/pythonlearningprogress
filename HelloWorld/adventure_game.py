start = input("Do you want to play the game? (Yes/no) ").lower()
if start == "yes":
    name = input("Type in your name: ")
    print("Welcome", name, "To the adventure!")
    begin = input(
        "You are on a dirt road, there's 2 path you can take. which way would you like to go (left/right)? "
    ).lower()

    if begin == "left":
        answer = input(
            "You saw a river that you can cross, do you want to walk around it or swim across? (type walk/swim) "
        ).lower()
        if answer == "walk":
            answer = input(
                "You tried to walk around it, but in the middle of it you saw a group of goblin. what would you do? (talk/sneak) "
            ).lower()
            if answer == "sneak":
                print(
                    "The goblin heard you and immediately shot an arrow at you, you're dead."
                )
            elif answer == "talk":
                print(
                    "The goblin able to talked your language and offer some help to get to the nearest city."
                )
        elif answer == "swim":
            print("You swam across the river but were eaten by an alligator.")
        else:
            print("Not a valid option, the game is over.")

    elif begin == "right":
        answer = input(
            "You saw a forest in the distance, would you like to keep walk towards it or observe for a while? (walk/observe)"
        ).lower()
        if answer == "walk":
            print(
                "You walked right into a bandit trap, they instantly shot you with arrows. Game over."
            )
        elif answer == "observe":
            answer = input(
                "You saw some bandit waiting to ambush you in the distance. what do you want to do? (sneak/turn around)"
            ).lower()
            if answer == "sneak":
                print(
                    "You were able to sneak around a bandit and kill him silently. what are you going to do now? (loot/hide)"
                )
            elif answer == "turn around":
                print("You decided to turn around and took the other way. Game over.")

    else:
        print("Not a valid option, the game is over.")

else:
    quit()
