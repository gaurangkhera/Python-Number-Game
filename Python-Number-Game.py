import random


while True:
    computerNumberGen = random.randint(1,6)
    playerNumberGen = random.randint(1,6)

    print("The computer rolled", computerNumberGen)
    print("The player rolled", playerNumberGen)

    if playerNumberGen == computerNumberGen:
        print("The player's random number is equal to the computer's random number!!")

    choice = input("Do you want to play again or exit the game?")
    if choice == "exit":
        break
