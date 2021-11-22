import random
points = 0
games_played = 0
while True:
    games_played += 1
    user_turn = input("enter r for rock, p for paper and s for scissors -> \n")
    computer_turn = random.randint(1, 3) # 1 = r, 2 = p , 3 = s
    if computer_turn == 1:
        if user_turn == "p":
            print("you won")
            points += 1
        else:
            print("you lost")

    elif computer_turn == 2:
        if user_turn == "s":
            print("you won")
            points += 1
        else:
            print("you lost")

    elif computer_turn == 3:
        if user_turn == "r":
            print("you won")
            points += 1
        else:
            print("you lost")

    opinion = input("If you want to continue, Enter y, Else, enter n\n")
    if opinion == "y":

        continue
    elif opinion == "n":
        print(f"You played {games_played} matches. \nYou won {points} of them.\nThe win percentage is {int((points/games_played) * 100)}% \n")
        break
    else:
        print("As the input is not defined, The game will restart...")


input("Press enter to exit...")