import random

def runGame(playerChoice):
    playerChoice = int(playerChoice)
    comChoice = random.randint(1 , 3)
    if (playerChoice == comChoice):
        print("Draw")
    elif (comChoice == 1 and playerChoice == 2):
        print("The another player choose Rock")
        print("You Won")
    elif (comChoice == 1 and playerChoice == 3):
        print("The another player choose Rock")
        print("Game Over")
    elif (comChoice == 2 and playerChoice == 1):
        print("The another player choose Paper")
        print("Game Over")
    elif (comChoice == 2 and playerChoice == 3):
        print("The another player choose Paper")
        print("You Won")
    elif (comChoice == 3 and playerChoice == 1):
        print("The another player choose Scissor")
        print("You Won")
    elif (comChoice == 3 and playerChoice == 2):
        print("The another player choose Scissor")
        print("Game Over")

print("(1) Rock (2) Paper (3)Scissor")
choice = input("Enter your choice: ")
runGame(choice)