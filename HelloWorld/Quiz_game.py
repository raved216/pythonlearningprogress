print("Welcome to the quiz!")

playing = input("Do you want to play? (Y/N) ")

if playing.lower() != "y":
    quit()

print("Let's play!")
score = 0

answer = input("Where is Jabba the hutt from? ")
if answer.lower() == "tatooine":
    print("Correct!")
    score += 1
else:
    print("False!")

answer2 = input("What is the iconic Jedi weapon? ")
if answer2.lower() == "lightsaber":
    print("Correct!")
    score += 1
else:
    print("False!")

answer3 = input("What is the the planet destroyer called? ")
if answer3.lower() == "deathstar":
    print("Correct!")
    score += 1
else:
    print("False!")

answer4 = input("What is the color of Darth Vader? ")
if answer4.lower() == "black":
    print("Correct!")
    score += 1
else:
    print("False!")

print("You got " + str(score) + " question(s) correct.y")
print("You got " + str((score/4) * 100) + "%.")